# gRPC Distributed Drone Demo

### Overview

This project demonstrates a simple **cross-language gRPC communication** setup between two services in a simulated drone system.

While the same functionality could be achieved with REST and JSON, gRPC offers a much more efficient and structured approach - using binary Protocol Buffers and HTTP/2 for faster, type-safe communication between different services and languages.

**System parts:**

* **C++ Client (DroneManager)** - manages a fleet of drones and sends image data for analysis.
* **Python Server (ImageAnalyzer)** - receives image data and returns a mock analysis result.

The goal is to illustrate how gRPC allows efficient and structured communication between services written in different programming languages.

---

### System Flow

1. The **DroneManager** holds a list of active drones, each with an image file reference.
2. A random drone "captures" an image and sends it via gRPC to the Python service.
3. The **ImageAnalyzer** simulates image processing (e.g., detecting an object) and returns a result.
4. The client prints the detection result to the console.

---

### Folder Structure

```
gRPC-distributed-drone/
├── cpp_client/
│   └── drone_manager.cpp
│   └── (generated files: drone.pb.* and drone.grpc.pb.*)
│
└── python_server/
    └── drone.proto
    └── image_analyzer_server.py
    └── (generated files: drone_pb2.py and drone_pb2_grpc.py)
```

---

### Build & Run Instructions

#### 1. Generate protobuf and gRPC files

* **For Python:**

  ```bash
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. drone.proto
  ```
* **For C++:**

  ```bash
  protoc -I. --cpp_out=. --grpc_out=. --plugin=protoc-gen-grpc="C:\path\to\grpc_cpp_plugin.exe" drone.proto
  ```

#### 2. Run the Python server

```bash
python python_server/image_analyzer_server.py
```

#### 3. Build the C++ client

Using g++:

```bash
g++ -std=c++17 cpp_client/drone_manager.cpp cpp_client/drone.pb.cc cpp_client/drone.grpc.pb.cc -o drone_manager.exe ^
  -I"C:\path\to\include" -L"C:\path\to\lib" -lgrpc++ -lprotobuf -lgrpc -lgpr
```

Or use CMake if configured.

#### 4. Run the C++ client

```bash
./cpp_client/drone_manager.exe
```

---

### Example Output

**Server (Python):**

```
Python gRPC server running on port 50051...
Received image from drone D124, size=4821 bytes
Detected: Car (0.91)
```

**Client (C++):**

```
[Drone D124] -> Detected: Car (confidence: 0.91)
[Drone D125] -> Detected: Person (confidence: 0.85)
[Drone D123] -> Detected: Tree (confidence: 0.78)
```

---

### Summary

This project is a **minimal distributed demo** showing how gRPC can bridge communication between C++ and Python services, using a simulated drone fleet and an image analysis service. It serves as an educational example for gRPC, protobuf, and multi-language microservice integration.