# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from opensnitch.network import network_pb2 as opensnitch_dot_network_dot_network__pb2
from opensnitch.rules import rules_pb2 as opensnitch_dot_rules_dot_rules__pb2
from opensnitch.ui import ui_pb2 as opensnitch_dot_ui_dot_ui__pb2


class UIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/opensnitch.ui.UI/Ping',
        request_serializer=opensnitch_dot_ui_dot_ui__pb2.PingRequest.SerializeToString,
        response_deserializer=opensnitch_dot_ui_dot_ui__pb2.PingReply.FromString,
        )
    self.AskRule = channel.unary_unary(
        '/opensnitch.ui.UI/AskRule',
        request_serializer=opensnitch_dot_network_dot_network__pb2.Connection.SerializeToString,
        response_deserializer=opensnitch_dot_rules_dot_rules__pb2.Rule.FromString,
        )


class UIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AskRule(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=opensnitch_dot_ui_dot_ui__pb2.PingRequest.FromString,
          response_serializer=opensnitch_dot_ui_dot_ui__pb2.PingReply.SerializeToString,
      ),
      'AskRule': grpc.unary_unary_rpc_method_handler(
          servicer.AskRule,
          request_deserializer=opensnitch_dot_network_dot_network__pb2.Connection.FromString,
          response_serializer=opensnitch_dot_rules_dot_rules__pb2.Rule.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'opensnitch.ui.UI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
