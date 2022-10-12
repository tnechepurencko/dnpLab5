# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chord_pb2 as chord__pb2


class RegistryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/Registry/register',
                request_serializer=chord__pb2.RegisterRequest.SerializeToString,
                response_deserializer=chord__pb2.RegisterReply.FromString,
                )
        self.deregister = channel.unary_unary(
                '/Registry/deregister',
                request_serializer=chord__pb2.DeregisterRequest.SerializeToString,
                response_deserializer=chord__pb2.DeregisterReply.FromString,
                )
        self.populate_finger_table = channel.unary_unary(
                '/Registry/populate_finger_table',
                request_serializer=chord__pb2.PFTRequest.SerializeToString,
                response_deserializer=chord__pb2.PFTReply.FromString,
                )
        self.get_chord_info = channel.unary_unary(
                '/Registry/get_chord_info',
                request_serializer=chord__pb2.Empty.SerializeToString,
                response_deserializer=chord__pb2.GCIReply.FromString,
                )
        self.who_am_i = channel.unary_unary(
                '/Registry/who_am_i',
                request_serializer=chord__pb2.Empty.SerializeToString,
                response_deserializer=chord__pb2.WAIResponse.FromString,
                )


class RegistryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deregister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def populate_finger_table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_chord_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def who_am_i(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=chord__pb2.RegisterRequest.FromString,
                    response_serializer=chord__pb2.RegisterReply.SerializeToString,
            ),
            'deregister': grpc.unary_unary_rpc_method_handler(
                    servicer.deregister,
                    request_deserializer=chord__pb2.DeregisterRequest.FromString,
                    response_serializer=chord__pb2.DeregisterReply.SerializeToString,
            ),
            'populate_finger_table': grpc.unary_unary_rpc_method_handler(
                    servicer.populate_finger_table,
                    request_deserializer=chord__pb2.PFTRequest.FromString,
                    response_serializer=chord__pb2.PFTReply.SerializeToString,
            ),
            'get_chord_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_chord_info,
                    request_deserializer=chord__pb2.Empty.FromString,
                    response_serializer=chord__pb2.GCIReply.SerializeToString,
            ),
            'who_am_i': grpc.unary_unary_rpc_method_handler(
                    servicer.who_am_i,
                    request_deserializer=chord__pb2.Empty.FromString,
                    response_serializer=chord__pb2.WAIResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Registry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Registry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Registry/register',
            chord__pb2.RegisterRequest.SerializeToString,
            chord__pb2.RegisterReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deregister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Registry/deregister',
            chord__pb2.DeregisterRequest.SerializeToString,
            chord__pb2.DeregisterReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def populate_finger_table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Registry/populate_finger_table',
            chord__pb2.PFTRequest.SerializeToString,
            chord__pb2.PFTReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_chord_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Registry/get_chord_info',
            chord__pb2.Empty.SerializeToString,
            chord__pb2.GCIReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def who_am_i(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Registry/who_am_i',
            chord__pb2.Empty.SerializeToString,
            chord__pb2.WAIResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_finger_table = channel.unary_unary(
                '/Node/get_finger_table',
                request_serializer=chord__pb2.Empty.SerializeToString,
                response_deserializer=chord__pb2.GFTReply.FromString,
                )
        self.save = channel.unary_unary(
                '/Node/save',
                request_serializer=chord__pb2.SaveRequest.SerializeToString,
                response_deserializer=chord__pb2.SaveReply.FromString,
                )
        self.remove = channel.unary_unary(
                '/Node/remove',
                request_serializer=chord__pb2.RemoveRequest.SerializeToString,
                response_deserializer=chord__pb2.RemoveReply.FromString,
                )
        self.find = channel.unary_unary(
                '/Node/find',
                request_serializer=chord__pb2.FindRequest.SerializeToString,
                response_deserializer=chord__pb2.FindReply.FromString,
                )
        self.who_am_i = channel.unary_unary(
                '/Node/who_am_i',
                request_serializer=chord__pb2.Empty.SerializeToString,
                response_deserializer=chord__pb2.WAIResponse.FromString,
                )


class NodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_finger_table(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def who_am_i(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_finger_table': grpc.unary_unary_rpc_method_handler(
                    servicer.get_finger_table,
                    request_deserializer=chord__pb2.Empty.FromString,
                    response_serializer=chord__pb2.GFTReply.SerializeToString,
            ),
            'save': grpc.unary_unary_rpc_method_handler(
                    servicer.save,
                    request_deserializer=chord__pb2.SaveRequest.FromString,
                    response_serializer=chord__pb2.SaveReply.SerializeToString,
            ),
            'remove': grpc.unary_unary_rpc_method_handler(
                    servicer.remove,
                    request_deserializer=chord__pb2.RemoveRequest.FromString,
                    response_serializer=chord__pb2.RemoveReply.SerializeToString,
            ),
            'find': grpc.unary_unary_rpc_method_handler(
                    servicer.find,
                    request_deserializer=chord__pb2.FindRequest.FromString,
                    response_serializer=chord__pb2.FindReply.SerializeToString,
            ),
            'who_am_i': grpc.unary_unary_rpc_method_handler(
                    servicer.who_am_i,
                    request_deserializer=chord__pb2.Empty.FromString,
                    response_serializer=chord__pb2.WAIResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Node', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Node(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_finger_table(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Node/get_finger_table',
            chord__pb2.Empty.SerializeToString,
            chord__pb2.GFTReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Node/save',
            chord__pb2.SaveRequest.SerializeToString,
            chord__pb2.SaveReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Node/remove',
            chord__pb2.RemoveRequest.SerializeToString,
            chord__pb2.RemoveReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Node/find',
            chord__pb2.FindRequest.SerializeToString,
            chord__pb2.FindReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def who_am_i(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Node/who_am_i',
            chord__pb2.Empty.SerializeToString,
            chord__pb2.WAIResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
