
from concurrent import futures
import grpc

from server_stub import add_nums_pb2_grpc, add_nums_pb2


class AddNumberServicer(add_nums_pb2_grpc.AddNumbersServicer):
    def AddNum(self, request, context):
        c = request.a+request.b
        return add_nums_pb2.Sum(c=c)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_nums_pb2_grpc.add_AddNumbersServicer_to_server(AddNumberServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
