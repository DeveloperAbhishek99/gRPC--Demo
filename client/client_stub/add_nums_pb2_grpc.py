# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import add_nums_pb2 as add__nums__pb2


class AddNumbersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddNum = channel.unary_unary(
                '/AddNumbers/AddNum',
                request_serializer=add__nums__pb2.Number.SerializeToString,
                response_deserializer=add__nums__pb2.Sum.FromString,
                )


class AddNumbersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddNum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AddNumbersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddNum': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNum,
                    request_deserializer=add__nums__pb2.Number.FromString,
                    response_serializer=add__nums__pb2.Sum.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'AddNumbers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AddNumbers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddNum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/AddNumbers/AddNum',
            add__nums__pb2.Number.SerializeToString,
            add__nums__pb2.Sum.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
