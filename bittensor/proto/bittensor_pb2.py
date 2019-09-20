# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bittensor/proto/bittensor.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='bittensor/proto/bittensor.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1f\x62ittensor/proto/bittensor.proto\"F\n\x0cSpikeRequest\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\x0c\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\"F\n\rSpikeResponse\x12\x10\n\x08\x63hild_id\x18\x03 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\x0c\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\"F\n\x0cGradeRequest\x12\x11\n\tparent_id\x18\x03 \x01(\t\x12\x12\n\nmessage_id\x18\x06 \x01(\x0c\x12\x0f\n\x07payload\x18\x07 \x01(\x0c\"\x1f\n\rGradeResponse\x12\x0e\n\x06\x61\x63\x63\x65pt\x18\x01 \x01(\x08\x32_\n\tBittensor\x12(\n\x05Spike\x12\r.SpikeRequest\x1a\x0e.SpikeResponse\"\x00\x12(\n\x05Grade\x12\r.GradeRequest\x1a\x0e.GradeResponse\"\x00\x62\x06proto3'
    ))

_SPIKEREQUEST = _descriptor.Descriptor(
    name='SpikeRequest',
    full_name='SpikeRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='parent_id',
                                    full_name='SpikeRequest.parent_id',
                                    index=0,
                                    number=3,
                                    type=9,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b("").decode('utf-8'),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='message_id',
                                    full_name='SpikeRequest.message_id',
                                    index=1,
                                    number=6,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='payload',
                                    full_name='SpikeRequest.payload',
                                    index=2,
                                    number=7,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=35,
    serialized_end=105,
)

_SPIKERESPONSE = _descriptor.Descriptor(
    name='SpikeResponse',
    full_name='SpikeResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='child_id',
                                    full_name='SpikeResponse.child_id',
                                    index=0,
                                    number=3,
                                    type=9,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b("").decode('utf-8'),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='message_id',
                                    full_name='SpikeResponse.message_id',
                                    index=1,
                                    number=6,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='payload',
                                    full_name='SpikeResponse.payload',
                                    index=2,
                                    number=7,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=107,
    serialized_end=177,
)

_GRADEREQUEST = _descriptor.Descriptor(
    name='GradeRequest',
    full_name='GradeRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='parent_id',
                                    full_name='GradeRequest.parent_id',
                                    index=0,
                                    number=3,
                                    type=9,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b("").decode('utf-8'),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='message_id',
                                    full_name='GradeRequest.message_id',
                                    index=1,
                                    number=6,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
        _descriptor.FieldDescriptor(name='payload',
                                    full_name='GradeRequest.payload',
                                    index=2,
                                    number=7,
                                    type=12,
                                    cpp_type=9,
                                    label=1,
                                    has_default_value=False,
                                    default_value=_b(""),
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=179,
    serialized_end=249,
)

_GRADERESPONSE = _descriptor.Descriptor(
    name='GradeResponse',
    full_name='GradeResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(name='accept',
                                    full_name='GradeResponse.accept',
                                    index=0,
                                    number=1,
                                    type=8,
                                    cpp_type=7,
                                    label=1,
                                    has_default_value=False,
                                    default_value=False,
                                    message_type=None,
                                    enum_type=None,
                                    containing_type=None,
                                    is_extension=False,
                                    extension_scope=None,
                                    serialized_options=None,
                                    file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=251,
    serialized_end=282,
)

DESCRIPTOR.message_types_by_name['SpikeRequest'] = _SPIKEREQUEST
DESCRIPTOR.message_types_by_name['SpikeResponse'] = _SPIKERESPONSE
DESCRIPTOR.message_types_by_name['GradeRequest'] = _GRADEREQUEST
DESCRIPTOR.message_types_by_name['GradeResponse'] = _GRADERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpikeRequest = _reflection.GeneratedProtocolMessageType(
    'SpikeRequest',
    (_message.Message,),
    dict(DESCRIPTOR=_SPIKEREQUEST,
         __module__='bittensor.proto.bittensor_pb2'
         # @@protoc_insertion_point(class_scope:SpikeRequest)
        ))
_sym_db.RegisterMessage(SpikeRequest)

SpikeResponse = _reflection.GeneratedProtocolMessageType(
    'SpikeResponse',
    (_message.Message,),
    dict(DESCRIPTOR=_SPIKERESPONSE,
         __module__='bittensor.proto.bittensor_pb2'
         # @@protoc_insertion_point(class_scope:SpikeResponse)
        ))
_sym_db.RegisterMessage(SpikeResponse)

GradeRequest = _reflection.GeneratedProtocolMessageType(
    'GradeRequest',
    (_message.Message,),
    dict(DESCRIPTOR=_GRADEREQUEST,
         __module__='bittensor.proto.bittensor_pb2'
         # @@protoc_insertion_point(class_scope:GradeRequest)
        ))
_sym_db.RegisterMessage(GradeRequest)

GradeResponse = _reflection.GeneratedProtocolMessageType(
    'GradeResponse',
    (_message.Message,),
    dict(DESCRIPTOR=_GRADERESPONSE,
         __module__='bittensor.proto.bittensor_pb2'
         # @@protoc_insertion_point(class_scope:GradeResponse)
        ))
_sym_db.RegisterMessage(GradeResponse)

_BITTENSOR = _descriptor.ServiceDescriptor(name='Bittensor',
                                           full_name='Bittensor',
                                           file=DESCRIPTOR,
                                           index=0,
                                           serialized_options=None,
                                           serialized_start=284,
                                           serialized_end=379,
                                           methods=[
                                               _descriptor.MethodDescriptor(
                                                   name='Spike',
                                                   full_name='Bittensor.Spike',
                                                   index=0,
                                                   containing_service=None,
                                                   input_type=_SPIKEREQUEST,
                                                   output_type=_SPIKERESPONSE,
                                                   serialized_options=None,
                                               ),
                                               _descriptor.MethodDescriptor(
                                                   name='Grade',
                                                   full_name='Bittensor.Grade',
                                                   index=1,
                                                   containing_service=None,
                                                   input_type=_GRADEREQUEST,
                                                   output_type=_GRADERESPONSE,
                                                   serialized_options=None,
                                               ),
                                           ])
_sym_db.RegisterServiceDescriptor(_BITTENSOR)

DESCRIPTOR.services_by_name['Bittensor'] = _BITTENSOR

# @@protoc_insertion_point(module_scope)
