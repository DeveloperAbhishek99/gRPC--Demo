
import grpc
from client_stub import add_nums_pb2,add_nums_pb2_grpc


def add_numbers(stub):
    try:
        Number = add_nums_pb2.Number(a= 1,b = 2)
        Sum = stub.AddNum(Number)
        print(Sum)
    except Exception as e:
        print(e)



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = add_nums_pb2_grpc.AddNumbersStub(channel)
        print("-------------- Adding Numbers--------------")
        add_numbers(stub)


if __name__ == '__main__':
    run()
