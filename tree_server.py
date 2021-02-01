import json
import grpc
from generated.tree_pb2_grpc import (
    TreeServiceServicer,
    add_TreeServiceServicer_to_server,
)
from generated.tree_pb2 import TreeList, TreeRequest, Tree
from concurrent import futures
import logging

with open("bomen1.json") as fp:
    trees = json.load(fp)["features"]


def tree_list(n=None):
    """Return first n trees"""
    result = []
    for doc in trees[: (n or len(trees))]:
        props = doc["properties"]
        lat, lon = doc["geometry"]["coordinates"]
        result.append(Tree(id=doc["id"], latitude=lat, longitude=lon, **props))
    return result


class TreeServer(TreeServiceServicer):
    def getTrees(self, request, context):
        return TreeList(data=tree_list(request.n))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TreeServiceServicer_to_server(TreeServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
    logging.basicConfig()