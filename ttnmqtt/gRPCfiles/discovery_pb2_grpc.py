# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import .discovery_pb2 as github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DiscoveryStub(object):
  """The Discovery service is used to discover services within The Things Network.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Announce = channel.unary_unary(
        '/discovery.Discovery/Announce',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetAll = channel.unary_unary(
        '/discovery.Discovery/GetAll',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetServiceRequest.SerializeToString,
        response_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.AnnouncementsResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/discovery.Discovery/Get',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetRequest.SerializeToString,
        response_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.FromString,
        )
    self.AddMetadata = channel.unary_unary(
        '/discovery.Discovery/AddMetadata',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.MetadataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteMetadata = channel.unary_unary(
        '/discovery.Discovery/DeleteMetadata',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.MetadataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetByAppID = channel.unary_unary(
        '/discovery.Discovery/GetByAppID',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByAppIDRequest.SerializeToString,
        response_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.FromString,
        )
    self.GetByGatewayID = channel.unary_unary(
        '/discovery.Discovery/GetByGatewayID',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByGatewayIDRequest.SerializeToString,
        response_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.FromString,
        )
    self.GetByAppEUI = channel.unary_unary(
        '/discovery.Discovery/GetByAppEUI',
        request_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByAppEUIRequest.SerializeToString,
        response_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.FromString,
        )


class DiscoveryServicer(object):
  """The Discovery service is used to discover services within The Things Network.
  """

  def Announce(self, request, context):
    """Announce a component to the Discovery server.
    A call to `Announce` does not processes the `metadata` field, so you can safely leave this field empty.
    Adding or removing Metadata should be done with the `AddMetadata` and `DeleteMetadata` methods.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAll(self, request, context):
    """Get all announcements for a specific service type
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get a specific announcement
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddMetadata(self, request, context):
    """Add metadata to an announement
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMetadata(self, request, context):
    """Delete metadata from an announcement
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByAppID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByGatewayID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetByAppEUI(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiscoveryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Announce': grpc.unary_unary_rpc_method_handler(
          servicer.Announce,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetAll': grpc.unary_unary_rpc_method_handler(
          servicer.GetAll,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetServiceRequest.FromString,
          response_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.AnnouncementsResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetRequest.FromString,
          response_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.SerializeToString,
      ),
      'AddMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.AddMetadata,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.MetadataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMetadata,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.MetadataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetByAppID': grpc.unary_unary_rpc_method_handler(
          servicer.GetByAppID,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByAppIDRequest.FromString,
          response_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.SerializeToString,
      ),
      'GetByGatewayID': grpc.unary_unary_rpc_method_handler(
          servicer.GetByGatewayID,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByGatewayIDRequest.FromString,
          response_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.SerializeToString,
      ),
      'GetByAppEUI': grpc.unary_unary_rpc_method_handler(
          servicer.GetByAppEUI,
          request_deserializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.GetByAppEUIRequest.FromString,
          response_serializer=github__com_dot_TheThingsNetwork_dot_api_dot_discovery_dot_discovery__pb2.Announcement.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'discovery.Discovery', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class DiscoveryManagerStub(object):
  """The DiscoveryManager service provides configuration and monitoring functionality
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class DiscoveryManagerServicer(object):
  """The DiscoveryManager service provides configuration and monitoring functionality
  """


def add_DiscoveryManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'discovery.DiscoveryManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
