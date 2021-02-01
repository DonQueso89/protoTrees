import grpc
from generated.tree_pb2_grpc import TreeServiceStub
from generated.tree_pb2 import TreeRequest


def run():
    channel = grpc.insecure_channel("localhost:50051")
    api = TreeServiceStub(channel)
    print(api.getTrees(TreeRequest(n=3)))


if __name__ == "__main__":
    run()