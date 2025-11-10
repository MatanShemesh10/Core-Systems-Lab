import grpc
from concurrent import futures
import drone_pb2
import drone_pb2_grpc
import random
import time

class ImageAnalyzerServicer(drone_pb2_grpc.ImageAnalyzerServicer):
    def AnalyzeObject(self, request, context):
        print(f"Received image from drone {request.drone_id}, size={len(request.image)} bytes")
        labels = ["Car", "Person", "Tree", "Building"]
        label = random.choice(labels)
        confidence = round(random.uniform(0.7, 0.99), 2)
        print(f"Detected: {label} ({confidence})")
        return drone_pb2.AnalysisResult(label=label, confidence=confidence)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    drone_pb2_grpc.add_ImageAnalyzerServicer_to_server(ImageAnalyzerServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Python gRPC server running on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
