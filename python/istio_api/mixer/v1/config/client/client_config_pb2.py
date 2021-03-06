# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/v1/config/client/client_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from mixer.v1 import attributes_pb2 as mixer_dot_v1_dot_attributes__pb2
from mixer.v1.config.client import api_spec_pb2 as mixer_dot_v1_dot_config_dot_client_dot_api__spec__pb2
from mixer.v1.config.client import quota_pb2 as mixer_dot_v1_dot_config_dot_client_dot_quota__pb2
from mixer.v1.config.client import auth_pb2 as mixer_dot_v1_dot_config_dot_client_dot_auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/v1/config/client/client_config.proto',
  package='istio.mixer.v1.config.client',
  syntax='proto3',
  serialized_pb=_b('\n*mixer/v1/config/client/client_config.proto\x12\x1cistio.mixer.v1.config.client\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19mixer/v1/attributes.proto\x1a%mixer/v1/config/client/api_spec.proto\x1a\"mixer/v1/config/client/quota.proto\x1a!mixer/v1/config/client/auth.proto\"\x8c\x01\n\x11NetworkFailPolicy\x12J\n\x06policy\x18\x01 \x01(\x0e\x32:.istio.mixer.v1.config.client.NetworkFailPolicy.FailPolicy\"+\n\nFailPolicy\x12\r\n\tFAIL_OPEN\x10\x00\x12\x0e\n\nFAIL_CLOSE\x10\x01\"\xa9\x03\n\rServiceConfig\x12\x1b\n\x13\x64isable_check_calls\x18\x01 \x01(\x08\x12\x1c\n\x14\x64isable_report_calls\x18\x02 \x01(\x08\x12\x34\n\x10mixer_attributes\x18\x03 \x01(\x0b\x32\x1a.istio.mixer.v1.Attributes\x12@\n\rhttp_api_spec\x18\x04 \x03(\x0b\x32).istio.mixer.v1.config.client.HTTPAPISpec\x12;\n\nquota_spec\x18\x05 \x03(\x0b\x32\'.istio.mixer.v1.config.client.QuotaSpec\x12Z\n\x13\x65nd_user_authn_spec\x18\x06 \x01(\x0b\x32=.istio.mixer.v1.config.client.EndUserAuthenticationPolicySpec\x12L\n\x13network_fail_policy\x18\x07 \x01(\x0b\x32/.istio.mixer.v1.config.client.NetworkFailPolicy\"\xa0\x02\n\x0fTransportConfig\x12\x1b\n\x13\x64isable_check_cache\x18\x01 \x01(\x08\x12\x1b\n\x13\x64isable_quota_cache\x18\x02 \x01(\x08\x12\x1c\n\x14\x64isable_report_batch\x18\x03 \x01(\x08\x12L\n\x13network_fail_policy\x18\x04 \x01(\x0b\x32/.istio.mixer.v1.config.client.NetworkFailPolicy\x12\x38\n\x15stats_update_interval\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x15\n\rcheck_cluster\x18\x06 \x01(\t\x12\x16\n\x0ereport_cluster\x18\x07 \x01(\t\"\xa8\x03\n\x10HttpClientConfig\x12@\n\ttransport\x18\x01 \x01(\x0b\x32-.istio.mixer.v1.config.client.TransportConfig\x12[\n\x0fservice_configs\x18\x02 \x03(\x0b\x32\x42.istio.mixer.v1.config.client.HttpClientConfig.ServiceConfigsEntry\x12#\n\x1b\x64\x65\x66\x61ult_destination_service\x18\x03 \x01(\t\x12\x34\n\x10mixer_attributes\x18\x04 \x01(\x0b\x32\x1a.istio.mixer.v1.Attributes\x12\x36\n\x12\x66orward_attributes\x18\x05 \x01(\x0b\x32\x1a.istio.mixer.v1.Attributes\x1a\x62\n\x13ServiceConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b\x32+.istio.mixer.v1.config.client.ServiceConfig:\x02\x38\x01\"\xc0\x02\n\x0fTcpClientConfig\x12@\n\ttransport\x18\x01 \x01(\x0b\x32-.istio.mixer.v1.config.client.TransportConfig\x12\x34\n\x10mixer_attributes\x18\x02 \x01(\x0b\x32\x1a.istio.mixer.v1.Attributes\x12\x1b\n\x13\x64isable_check_calls\x18\x03 \x01(\x08\x12\x1c\n\x14\x64isable_report_calls\x18\x04 \x01(\x08\x12\x46\n\x15\x63onnection_quota_spec\x18\x05 \x01(\x0b\x32\'.istio.mixer.v1.config.client.QuotaSpec\x12\x32\n\x0freport_interval\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB1Z#istio.io/api/mixer/v1/config/client\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,mixer_dot_v1_dot_attributes__pb2.DESCRIPTOR,mixer_dot_v1_dot_config_dot_client_dot_api__spec__pb2.DESCRIPTOR,mixer_dot_v1_dot_config_dot_client_dot_quota__pb2.DESCRIPTOR,mixer_dot_v1_dot_config_dot_client_dot_auth__pb2.DESCRIPTOR,])



_NETWORKFAILPOLICY_FAILPOLICY = _descriptor.EnumDescriptor(
  name='FailPolicy',
  full_name='istio.mixer.v1.config.client.NetworkFailPolicy.FailPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAIL_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL_CLOSE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=365,
  serialized_end=408,
)
_sym_db.RegisterEnumDescriptor(_NETWORKFAILPOLICY_FAILPOLICY)


_NETWORKFAILPOLICY = _descriptor.Descriptor(
  name='NetworkFailPolicy',
  full_name='istio.mixer.v1.config.client.NetworkFailPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='istio.mixer.v1.config.client.NetworkFailPolicy.policy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKFAILPOLICY_FAILPOLICY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=408,
)


_SERVICECONFIG = _descriptor.Descriptor(
  name='ServiceConfig',
  full_name='istio.mixer.v1.config.client.ServiceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disable_check_calls', full_name='istio.mixer.v1.config.client.ServiceConfig.disable_check_calls', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_report_calls', full_name='istio.mixer.v1.config.client.ServiceConfig.disable_report_calls', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixer_attributes', full_name='istio.mixer.v1.config.client.ServiceConfig.mixer_attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_api_spec', full_name='istio.mixer.v1.config.client.ServiceConfig.http_api_spec', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota_spec', full_name='istio.mixer.v1.config.client.ServiceConfig.quota_spec', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_user_authn_spec', full_name='istio.mixer.v1.config.client.ServiceConfig.end_user_authn_spec', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_fail_policy', full_name='istio.mixer.v1.config.client.ServiceConfig.network_fail_policy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=836,
)


_TRANSPORTCONFIG = _descriptor.Descriptor(
  name='TransportConfig',
  full_name='istio.mixer.v1.config.client.TransportConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disable_check_cache', full_name='istio.mixer.v1.config.client.TransportConfig.disable_check_cache', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_quota_cache', full_name='istio.mixer.v1.config.client.TransportConfig.disable_quota_cache', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_report_batch', full_name='istio.mixer.v1.config.client.TransportConfig.disable_report_batch', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_fail_policy', full_name='istio.mixer.v1.config.client.TransportConfig.network_fail_policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats_update_interval', full_name='istio.mixer.v1.config.client.TransportConfig.stats_update_interval', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_cluster', full_name='istio.mixer.v1.config.client.TransportConfig.check_cluster', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_cluster', full_name='istio.mixer.v1.config.client.TransportConfig.report_cluster', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=1127,
)


_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY = _descriptor.Descriptor(
  name='ServiceConfigsEntry',
  full_name='istio.mixer.v1.config.client.HttpClientConfig.ServiceConfigsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.v1.config.client.HttpClientConfig.ServiceConfigsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.config.client.HttpClientConfig.ServiceConfigsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1456,
  serialized_end=1554,
)

_HTTPCLIENTCONFIG = _descriptor.Descriptor(
  name='HttpClientConfig',
  full_name='istio.mixer.v1.config.client.HttpClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transport', full_name='istio.mixer.v1.config.client.HttpClientConfig.transport', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_configs', full_name='istio.mixer.v1.config.client.HttpClientConfig.service_configs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_destination_service', full_name='istio.mixer.v1.config.client.HttpClientConfig.default_destination_service', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixer_attributes', full_name='istio.mixer.v1.config.client.HttpClientConfig.mixer_attributes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forward_attributes', full_name='istio.mixer.v1.config.client.HttpClientConfig.forward_attributes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1130,
  serialized_end=1554,
)


_TCPCLIENTCONFIG = _descriptor.Descriptor(
  name='TcpClientConfig',
  full_name='istio.mixer.v1.config.client.TcpClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transport', full_name='istio.mixer.v1.config.client.TcpClientConfig.transport', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixer_attributes', full_name='istio.mixer.v1.config.client.TcpClientConfig.mixer_attributes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_check_calls', full_name='istio.mixer.v1.config.client.TcpClientConfig.disable_check_calls', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_report_calls', full_name='istio.mixer.v1.config.client.TcpClientConfig.disable_report_calls', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_quota_spec', full_name='istio.mixer.v1.config.client.TcpClientConfig.connection_quota_spec', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='report_interval', full_name='istio.mixer.v1.config.client.TcpClientConfig.report_interval', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1557,
  serialized_end=1877,
)

_NETWORKFAILPOLICY.fields_by_name['policy'].enum_type = _NETWORKFAILPOLICY_FAILPOLICY
_NETWORKFAILPOLICY_FAILPOLICY.containing_type = _NETWORKFAILPOLICY
_SERVICECONFIG.fields_by_name['mixer_attributes'].message_type = mixer_dot_v1_dot_attributes__pb2._ATTRIBUTES
_SERVICECONFIG.fields_by_name['http_api_spec'].message_type = mixer_dot_v1_dot_config_dot_client_dot_api__spec__pb2._HTTPAPISPEC
_SERVICECONFIG.fields_by_name['quota_spec'].message_type = mixer_dot_v1_dot_config_dot_client_dot_quota__pb2._QUOTASPEC
_SERVICECONFIG.fields_by_name['end_user_authn_spec'].message_type = mixer_dot_v1_dot_config_dot_client_dot_auth__pb2._ENDUSERAUTHENTICATIONPOLICYSPEC
_SERVICECONFIG.fields_by_name['network_fail_policy'].message_type = _NETWORKFAILPOLICY
_TRANSPORTCONFIG.fields_by_name['network_fail_policy'].message_type = _NETWORKFAILPOLICY
_TRANSPORTCONFIG.fields_by_name['stats_update_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY.fields_by_name['value'].message_type = _SERVICECONFIG
_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY.containing_type = _HTTPCLIENTCONFIG
_HTTPCLIENTCONFIG.fields_by_name['transport'].message_type = _TRANSPORTCONFIG
_HTTPCLIENTCONFIG.fields_by_name['service_configs'].message_type = _HTTPCLIENTCONFIG_SERVICECONFIGSENTRY
_HTTPCLIENTCONFIG.fields_by_name['mixer_attributes'].message_type = mixer_dot_v1_dot_attributes__pb2._ATTRIBUTES
_HTTPCLIENTCONFIG.fields_by_name['forward_attributes'].message_type = mixer_dot_v1_dot_attributes__pb2._ATTRIBUTES
_TCPCLIENTCONFIG.fields_by_name['transport'].message_type = _TRANSPORTCONFIG
_TCPCLIENTCONFIG.fields_by_name['mixer_attributes'].message_type = mixer_dot_v1_dot_attributes__pb2._ATTRIBUTES
_TCPCLIENTCONFIG.fields_by_name['connection_quota_spec'].message_type = mixer_dot_v1_dot_config_dot_client_dot_quota__pb2._QUOTASPEC
_TCPCLIENTCONFIG.fields_by_name['report_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['NetworkFailPolicy'] = _NETWORKFAILPOLICY
DESCRIPTOR.message_types_by_name['ServiceConfig'] = _SERVICECONFIG
DESCRIPTOR.message_types_by_name['TransportConfig'] = _TRANSPORTCONFIG
DESCRIPTOR.message_types_by_name['HttpClientConfig'] = _HTTPCLIENTCONFIG
DESCRIPTOR.message_types_by_name['TcpClientConfig'] = _TCPCLIENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkFailPolicy = _reflection.GeneratedProtocolMessageType('NetworkFailPolicy', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKFAILPOLICY,
  __module__ = 'mixer.v1.config.client.client_config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.NetworkFailPolicy)
  ))
_sym_db.RegisterMessage(NetworkFailPolicy)

ServiceConfig = _reflection.GeneratedProtocolMessageType('ServiceConfig', (_message.Message,), dict(
  DESCRIPTOR = _SERVICECONFIG,
  __module__ = 'mixer.v1.config.client.client_config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.ServiceConfig)
  ))
_sym_db.RegisterMessage(ServiceConfig)

TransportConfig = _reflection.GeneratedProtocolMessageType('TransportConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRANSPORTCONFIG,
  __module__ = 'mixer.v1.config.client.client_config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.TransportConfig)
  ))
_sym_db.RegisterMessage(TransportConfig)

HttpClientConfig = _reflection.GeneratedProtocolMessageType('HttpClientConfig', (_message.Message,), dict(

  ServiceConfigsEntry = _reflection.GeneratedProtocolMessageType('ServiceConfigsEntry', (_message.Message,), dict(
    DESCRIPTOR = _HTTPCLIENTCONFIG_SERVICECONFIGSENTRY,
    __module__ = 'mixer.v1.config.client.client_config_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.HttpClientConfig.ServiceConfigsEntry)
    ))
  ,
  DESCRIPTOR = _HTTPCLIENTCONFIG,
  __module__ = 'mixer.v1.config.client.client_config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.HttpClientConfig)
  ))
_sym_db.RegisterMessage(HttpClientConfig)
_sym_db.RegisterMessage(HttpClientConfig.ServiceConfigsEntry)

TcpClientConfig = _reflection.GeneratedProtocolMessageType('TcpClientConfig', (_message.Message,), dict(
  DESCRIPTOR = _TCPCLIENTCONFIG,
  __module__ = 'mixer.v1.config.client.client_config_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.TcpClientConfig)
  ))
_sym_db.RegisterMessage(TcpClientConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z#istio.io/api/mixer/v1/config/client\310\341\036\000\250\342\036\000\360\341\036\000'))
_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY.has_options = True
_HTTPCLIENTCONFIG_SERVICECONFIGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
