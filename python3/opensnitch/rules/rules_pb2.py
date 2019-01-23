# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opensnitch/rules/rules.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='opensnitch/rules/rules.proto',
  package='opensnitch.rules',
  syntax='proto3',
  serialized_options=_b('Z0github.com/Northern-Lights/os-rules-engine/rules'),
  serialized_pb=_b('\n\x1copensnitch/rules/rules.proto\x12\x10opensnitch.rules\"\x8f\x01\n\x04Rule\x12(\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x18.opensnitch.rules.Action\x12,\n\x08\x64uration\x18\x02 \x01(\x0e\x32\x1a.opensnitch.rules.Duration\x12/\n\tcondition\x18\x03 \x01(\x0b\x32\x1c.opensnitch.rules.Expression\"\xc5\x01\n\nExpression\x12\x0c\n\x04name\x18\x04 \x01(\t\x12.\n\toperation\x18\x01 \x01(\x0e\x32\x1b.opensnitch.rules.Operation\x12*\n\x04left\x18\x0e \x01(\x0b\x32\x1c.opensnitch.rules.Expression\x12+\n\x05right\x18\x0f \x01(\x0b\x32\x1c.opensnitch.rules.Expression\x12\x0f\n\x07strings\x18\x02 \x03(\t\x12\x0f\n\x07uint32s\x18\x03 \x03(\r*1\n\x06\x41\x63tion\x12\x12\n\x0e\x41\x43TION_UNKNOWN\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x12\x08\n\x04\x44\x45NY\x10\x02*L\n\x08\x44uration\x12\x14\n\x10\x44URATION_UNKNOWN\x10\x00\x12\x08\n\x04ONCE\x10\x01\x12\x14\n\x10\x46IREWALL_SESSION\x10\x02\x12\n\n\x06\x41LWAYS\x10\x03*\x91\x01\n\tOperation\x12\x15\n\x11OPERATION_UNKNOWN\x10\x00\x12\x08\n\x04TRUE\x10\t\x12\t\n\x05\x46\x41LSE\x10\n\x12\x07\n\x03\x41ND\x10\x01\x12\x06\n\x02OR\x10\x02\x12\x07\n\x03NOT\x10\x03\x12\n\n\x06\x44ST_IP\x10\x04\x12\x0c\n\x08\x44ST_HOST\x10\x05\x12\x0c\n\x08\x44ST_PORT\x10\x06\x12\r\n\tPROC_PATH\x10\x07\x12\x07\n\x03PID\x10\x08\x42\x32Z0github.com/Northern-Lights/os-rules-engine/rulesb\x06proto3')
)

_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='opensnitch.rules.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLOW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=396,
  serialized_end=445,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_DURATION = _descriptor.EnumDescriptor(
  name='Duration',
  full_name='opensnitch.rules.Duration',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DURATION_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIREWALL_SESSION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALWAYS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=447,
  serialized_end=523,
)
_sym_db.RegisterEnumDescriptor(_DURATION)

Duration = enum_type_wrapper.EnumTypeWrapper(_DURATION)
_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='opensnitch.rules.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATION_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUE', index=1, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALSE', index=2, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AND', index=3, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OR', index=4, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT', index=5, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DST_IP', index=6, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DST_HOST', index=7, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DST_PORT', index=8, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROC_PATH', index=9, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PID', index=10, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=526,
  serialized_end=671,
)
_sym_db.RegisterEnumDescriptor(_OPERATION)

Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
ACTION_UNKNOWN = 0
ALLOW = 1
DENY = 2
DURATION_UNKNOWN = 0
ONCE = 1
FIREWALL_SESSION = 2
ALWAYS = 3
OPERATION_UNKNOWN = 0
TRUE = 9
FALSE = 10
AND = 1
OR = 2
NOT = 3
DST_IP = 4
DST_HOST = 5
DST_PORT = 6
PROC_PATH = 7
PID = 8



_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='opensnitch.rules.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='opensnitch.rules.Rule.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='opensnitch.rules.Rule.duration', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='opensnitch.rules.Rule.condition', index=2,
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
  serialized_start=51,
  serialized_end=194,
)


_EXPRESSION = _descriptor.Descriptor(
  name='Expression',
  full_name='opensnitch.rules.Expression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='opensnitch.rules.Expression.name', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='opensnitch.rules.Expression.operation', index=1,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='opensnitch.rules.Expression.left', index=2,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='opensnitch.rules.Expression.right', index=3,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strings', full_name='opensnitch.rules.Expression.strings', index=4,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32s', full_name='opensnitch.rules.Expression.uint32s', index=5,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=197,
  serialized_end=394,
)

_RULE.fields_by_name['action'].enum_type = _ACTION
_RULE.fields_by_name['duration'].enum_type = _DURATION
_RULE.fields_by_name['condition'].message_type = _EXPRESSION
_EXPRESSION.fields_by_name['operation'].enum_type = _OPERATION
_EXPRESSION.fields_by_name['left'].message_type = _EXPRESSION
_EXPRESSION.fields_by_name['right'].message_type = _EXPRESSION
DESCRIPTOR.message_types_by_name['Rule'] = _RULE
DESCRIPTOR.message_types_by_name['Expression'] = _EXPRESSION
DESCRIPTOR.enum_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['Duration'] = _DURATION
DESCRIPTOR.enum_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Rule = _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), dict(
  DESCRIPTOR = _RULE,
  __module__ = 'opensnitch.rules.rules_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.rules.Rule)
  ))
_sym_db.RegisterMessage(Rule)

Expression = _reflection.GeneratedProtocolMessageType('Expression', (_message.Message,), dict(
  DESCRIPTOR = _EXPRESSION,
  __module__ = 'opensnitch.rules.rules_pb2'
  # @@protoc_insertion_point(class_scope:opensnitch.rules.Expression)
  ))
_sym_db.RegisterMessage(Expression)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
