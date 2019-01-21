# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opensnitch/ui/ui.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opensnitch.network import network_pb2 as opensnitch_dot_network_dot_network__pb2
from opensnitch.rules import rules_pb2 as opensnitch_dot_rules_dot_rules__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='opensnitch/ui/ui.proto',
  package='opensnitch.ui',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16opensnitch/ui/ui.proto\x12\ropensnitch.ui\x1a opensnitch/network/network.proto\x1a\x1copensnitch/rules/rules.proto\"C\n\x0bPingRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12(\n\x05stats\x18\x02 \x01(\x0b\x32\x19.opensnitch.ui.Statistics\"\x17\n\tPingReply\x12\n\n\x02id\x18\x01 \x01(\x04\"\xf6\x06\n\nStatistics\x12\x16\n\x0e\x64\x61\x65mon_version\x18\x01 \x01(\t\x12\r\n\x05rules\x18\x02 \x01(\x04\x12\x0e\n\x06uptime\x18\x03 \x01(\x04\x12\x15\n\rdns_responses\x18\x04 \x01(\x04\x12\x13\n\x0b\x63onnections\x18\x05 \x01(\x04\x12\x0f\n\x07ignored\x18\x06 \x01(\x04\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x07 \x01(\x04\x12\x0f\n\x07\x64ropped\x18\x08 \x01(\x04\x12\x11\n\trule_hits\x18\t \x01(\x04\x12\x13\n\x0brule_misses\x18\n \x01(\x04\x12\x38\n\x08\x62y_proto\x18\x0b \x03(\x0b\x32&.opensnitch.ui.Statistics.ByProtoEntry\x12<\n\nby_address\x18\x0c \x03(\x0b\x32(.opensnitch.ui.Statistics.ByAddressEntry\x12\x36\n\x07\x62y_host\x18\r \x03(\x0b\x32%.opensnitch.ui.Statistics.ByHostEntry\x12\x36\n\x07\x62y_port\x18\x0e \x03(\x0b\x32%.opensnitch.ui.Statistics.ByPortEntry\x12\x34\n\x06\x62y_uid\x18\x0f \x03(\x0b\x32$.opensnitch.ui.Statistics.ByUidEntry\x12\x42\n\rby_executable\x18\x10 \x03(\x0b\x32+.opensnitch.ui.Statistics.ByExecutableEntry\x12$\n\x06\x65vents\x18\x11 \x03(\x0b\x32\x14.opensnitch.ui.Event\x1a.\n\x0c\x42yProtoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x30\n\x0e\x42yAddressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a-\n\x0b\x42yHostEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a-\n\x0b\x42yPortEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a,\n\nByUidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x33\n\x11\x42yExecutableEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"o\n\x05\x45vent\x12\x0c\n\x04time\x18\x01 \x01(\t\x12\x32\n\nconnection\x18\x02 \x01(\x0b\x32\x1e.opensnitch.network.Connection\x12$\n\x04rule\x18\x03 \x01(\x0b\x32\x16.opensnitch.rules.Rule2\x89\x01\n\x02UI\x12>\n\x04Ping\x12\x1a.opensnitch.ui.PingRequest\x1a\x18.opensnitch.ui.PingReply\"\x00\x12\x43\n\x07\x41skRule\x12\x1e.opensnitch.network.Connection\x1a\x16.opensnitch.rules.Rule\"\x00\x62\x06proto3')
  ,
  dependencies=[opensnitch_dot_network_dot_network__pb2.DESCRIPTOR,opensnitch_dot_rules_dot_rules__pb2.DESCRIPTOR,])




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='opensnitch.ui.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='opensnitch.ui.PingRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='opensnitch.ui.PingRequest.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=172,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='opensnitch.ui.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='opensnitch.ui.PingReply.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=197,
)


_STATISTICS_BYPROTOENTRY = _descriptor.Descriptor(
  name='ByProtoEntry',
  full_name='opensnitch.ui.Statistics.ByProtoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByProtoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByProtoEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=797,
  serialized_end=843,
)

_STATISTICS_BYADDRESSENTRY = _descriptor.Descriptor(
  name='ByAddressEntry',
  full_name='opensnitch.ui.Statistics.ByAddressEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByAddressEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByAddressEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=893,
)

_STATISTICS_BYHOSTENTRY = _descriptor.Descriptor(
  name='ByHostEntry',
  full_name='opensnitch.ui.Statistics.ByHostEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByHostEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByHostEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=940,
)

_STATISTICS_BYPORTENTRY = _descriptor.Descriptor(
  name='ByPortEntry',
  full_name='opensnitch.ui.Statistics.ByPortEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByPortEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByPortEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=987,
)

_STATISTICS_BYUIDENTRY = _descriptor.Descriptor(
  name='ByUidEntry',
  full_name='opensnitch.ui.Statistics.ByUidEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByUidEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByUidEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=989,
  serialized_end=1033,
)

_STATISTICS_BYEXECUTABLEENTRY = _descriptor.Descriptor(
  name='ByExecutableEntry',
  full_name='opensnitch.ui.Statistics.ByExecutableEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='opensnitch.ui.Statistics.ByExecutableEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='opensnitch.ui.Statistics.ByExecutableEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1035,
  serialized_end=1086,
)

_STATISTICS = _descriptor.Descriptor(
  name='Statistics',
  full_name='opensnitch.ui.Statistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='daemon_version', full_name='opensnitch.ui.Statistics.daemon_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='opensnitch.ui.Statistics.rules', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uptime', full_name='opensnitch.ui.Statistics.uptime', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns_responses', full_name='opensnitch.ui.Statistics.dns_responses', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='opensnitch.ui.Statistics.connections', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignored', full_name='opensnitch.ui.Statistics.ignored', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accepted', full_name='opensnitch.ui.Statistics.accepted', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropped', full_name='opensnitch.ui.Statistics.dropped', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_hits', full_name='opensnitch.ui.Statistics.rule_hits', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_misses', full_name='opensnitch.ui.Statistics.rule_misses', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_proto', full_name='opensnitch.ui.Statistics.by_proto', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_address', full_name='opensnitch.ui.Statistics.by_address', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_host', full_name='opensnitch.ui.Statistics.by_host', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_port', full_name='opensnitch.ui.Statistics.by_port', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_uid', full_name='opensnitch.ui.Statistics.by_uid', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_executable', full_name='opensnitch.ui.Statistics.by_executable', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='opensnitch.ui.Statistics.events', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATISTICS_BYPROTOENTRY, _STATISTICS_BYADDRESSENTRY, _STATISTICS_BYHOSTENTRY, _STATISTICS_BYPORTENTRY, _STATISTICS_BYUIDENTRY, _STATISTICS_BYEXECUTABLEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=1086,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='opensnitch.ui.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='opensnitch.ui.Event.time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection', full_name='opensnitch.ui.Event.connection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='opensnitch.ui.Event.rule', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1088,
  serialized_end=1199,
)

_PINGREQUEST.fields_by_name['stats'].message_type = _STATISTICS
_STATISTICS_BYPROTOENTRY.containing_type = _STATISTICS
_STATISTICS_BYADDRESSENTRY.containing_type = _STATISTICS
_STATISTICS_BYHOSTENTRY.containing_type = _STATISTICS
_STATISTICS_BYPORTENTRY.containing_type = _STATISTICS
_STATISTICS_BYUIDENTRY.containing_type = _STATISTICS
_STATISTICS_BYEXECUTABLEENTRY.containing_type = _STATISTICS
_STATISTICS.fields_by_name['by_proto'].message_type = _STATISTICS_BYPROTOENTRY
_STATISTICS.fields_by_name['by_address'].message_type = _STATISTICS_BYADDRESSENTRY
_STATISTICS.fields_by_name['by_host'].message_type = _STATISTICS_BYHOSTENTRY
_STATISTICS.fields_by_name['by_port'].message_type = _STATISTICS_BYPORTENTRY
_STATISTICS.fields_by_name['by_uid'].message_type = _STATISTICS_BYUIDENTRY
_STATISTICS.fields_by_name['by_executable'].message_type = _STATISTICS_BYEXECUTABLEENTRY
_STATISTICS.fields_by_name['events'].message_type = _EVENT
_EVENT.fields_by_name['connection'].message_type = opensnitch_dot_network_dot_network__pb2._CONNECTION
_EVENT.fields_by_name['rule'].message_type = opensnitch_dot_rules_dot_rules__pb2._RULE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
DESCRIPTOR.message_types_by_name['Statistics'] = _STATISTICS
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'opensnitch.ui.ui_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.ui.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), dict(
  DESCRIPTOR = _PINGREPLY,
  __module__ = 'opensnitch.ui.ui_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.ui.PingReply)
  ))
_sym_db.RegisterMessage(PingReply)

Statistics = _reflection.GeneratedProtocolMessageType('Statistics', (_message.Message,), dict(

  ByProtoEntry = _reflection.GeneratedProtocolMessageType('ByProtoEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYPROTOENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByProtoEntry)
    ))
  ,

  ByAddressEntry = _reflection.GeneratedProtocolMessageType('ByAddressEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYADDRESSENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByAddressEntry)
    ))
  ,

  ByHostEntry = _reflection.GeneratedProtocolMessageType('ByHostEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYHOSTENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByHostEntry)
    ))
  ,

  ByPortEntry = _reflection.GeneratedProtocolMessageType('ByPortEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYPORTENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByPortEntry)
    ))
  ,

  ByUidEntry = _reflection.GeneratedProtocolMessageType('ByUidEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYUIDENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByUidEntry)
    ))
  ,

  ByExecutableEntry = _reflection.GeneratedProtocolMessageType('ByExecutableEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYEXECUTABLEENTRY,
    __module__ = 'opensnitch.ui.ui_pb2'
    # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics.ByExecutableEntry)
    ))
  ,
  DESCRIPTOR = _STATISTICS,
  __module__ = 'opensnitch.ui.ui_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.ui.Statistics)
  ))
_sym_db.RegisterMessage(Statistics)
_sym_db.RegisterMessage(Statistics.ByProtoEntry)
_sym_db.RegisterMessage(Statistics.ByAddressEntry)
_sym_db.RegisterMessage(Statistics.ByHostEntry)
_sym_db.RegisterMessage(Statistics.ByPortEntry)
_sym_db.RegisterMessage(Statistics.ByUidEntry)
_sym_db.RegisterMessage(Statistics.ByExecutableEntry)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'opensnitch.ui.ui_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.ui.Event)
  ))
_sym_db.RegisterMessage(Event)


_STATISTICS_BYPROTOENTRY._options = None
_STATISTICS_BYADDRESSENTRY._options = None
_STATISTICS_BYHOSTENTRY._options = None
_STATISTICS_BYPORTENTRY._options = None
_STATISTICS_BYUIDENTRY._options = None
_STATISTICS_BYEXECUTABLEENTRY._options = None

_UI = _descriptor.ServiceDescriptor(
  name='UI',
  full_name='opensnitch.ui.UI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1202,
  serialized_end=1339,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='opensnitch.ui.UI.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AskRule',
    full_name='opensnitch.ui.UI.AskRule',
    index=1,
    containing_service=None,
    input_type=opensnitch_dot_network_dot_network__pb2._CONNECTION,
    output_type=opensnitch_dot_rules_dot_rules__pb2._RULE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UI)

DESCRIPTOR.services_by_name['UI'] = _UI

# @@protoc_insertion_point(module_scope)