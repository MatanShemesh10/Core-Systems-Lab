#include <iostream>
#include <string>
#include <unordered_map>
#include <memory>
#include <random>
#include <fstream>
#include <grpcpp/grpcpp.h>
#include "drone.pb.h"
#include "drone.grpc.pb.h"

struct Drone {
    std::string id;
    std::string last_image_path;
};

class DroneManager {
public:
    DroneManager(std::shared_ptr<grpc::Channel> channel)
        : stub_(drone::ImageAnalyzer::NewStub(channel)) {
        // Initialize some active drones
        drones_["D123"] = {"D123", "sample1.jpg"};
        drones_["D124"] = {"D124", "sample2.jpg"};
        drones_["D125"] = {"D125", "sample3.jpg"};
    }

    void SendRandomDroneImage() {
        // Pick a random drone
        if (drones_.empty()) return;
        auto it = drones_.begin();
        std::advance(it, rand() % drones_.size());
        const Drone& drone = it->second;

        // Read image file (pretend)
        std::ifstream file(drone.last_image_path, std::ios::binary);
        if (!file.is_open()) {
            std::cerr << "Failed to open " << drone.last_image_path << std::endl;
            return;
        }
        std::string image_bytes((std::istreambuf_iterator<char>(file)),
                                std::istreambuf_iterator<char>());

        // Prepare request
        drone::ObjectData request;
        request.set_drone_id(drone.id);
        request.set_image(image_bytes);

        // Prepare response
        drone::AnalysisResult response;
        grpc::ClientContext context;

        // Send request
        grpc::Status status = stub_->AnalyzeObject(&context, request, &response);

        if (status.ok()) {
            std::cout << "[Drone " << drone.id << "] -> "
                      << "Detected: " << response.label()
                      << " (confidence: " << response.confidence() << ")"
                      << std::endl;
        } else {
            std::cerr << "RPC failed: " << status.error_message() << std::endl;
        }
    }

private:
    std::unique_ptr<drone::ImageAnalyzer::Stub> stub_;
    std::unordered_map<std::string, Drone> drones_;
};

int main() {
    auto channel = grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials());
    DroneManager manager(channel);

    for (int i = 0; i < 5; ++i) {
        manager.SendRandomDroneImage();
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
}
