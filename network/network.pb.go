// Code generated by protoc-gen-go. DO NOT EDIT.
// source: opensnitch/network/network.proto

package network

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Connection_Protocol int32

const (
	Connection_UNKNOWN Connection_Protocol = 0
	Connection_TCP     Connection_Protocol = 1
	Connection_UDP     Connection_Protocol = 2
)

var Connection_Protocol_name = map[int32]string{
	0: "UNKNOWN",
	1: "TCP",
	2: "UDP",
}

var Connection_Protocol_value = map[string]int32{
	"UNKNOWN": 0,
	"TCP":     1,
	"UDP":     2,
}

func (x Connection_Protocol) String() string {
	return proto.EnumName(Connection_Protocol_name, int32(x))
}

func (Connection_Protocol) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_36fc7553ab6b549b, []int{0, 0}
}

// Connection represents a network connection that the user is to decide
// whether to allow or deny
type Connection struct {
	Protocol             Connection_Protocol `protobuf:"varint,1,opt,name=protocol,proto3,enum=opensnitch.network.Connection_Protocol" json:"protocol,omitempty"`
	SrcIp                string              `protobuf:"bytes,2,opt,name=src_ip,json=srcIp,proto3" json:"src_ip,omitempty"`
	SrcPort              uint32              `protobuf:"varint,3,opt,name=src_port,json=srcPort,proto3" json:"src_port,omitempty"`
	DstIp                string              `protobuf:"bytes,4,opt,name=dst_ip,json=dstIp,proto3" json:"dst_ip,omitempty"`
	DstHost              string              `protobuf:"bytes,5,opt,name=dst_host,json=dstHost,proto3" json:"dst_host,omitempty"`
	DstPort              uint32              `protobuf:"varint,6,opt,name=dst_port,json=dstPort,proto3" json:"dst_port,omitempty"`
	UserId               uint32              `protobuf:"varint,7,opt,name=user_id,json=userId,proto3" json:"user_id,omitempty"`
	ProcessId            uint32              `protobuf:"varint,8,opt,name=process_id,json=processId,proto3" json:"process_id,omitempty"`
	ProcessPath          string              `protobuf:"bytes,9,opt,name=process_path,json=processPath,proto3" json:"process_path,omitempty"`
	ProcessArgs          []string            `protobuf:"bytes,10,rep,name=process_args,json=processArgs,proto3" json:"process_args,omitempty"`
	XXX_NoUnkeyedLiteral struct{}            `json:"-"`
	XXX_unrecognized     []byte              `json:"-"`
	XXX_sizecache        int32               `json:"-"`
}

func (m *Connection) Reset()         { *m = Connection{} }
func (m *Connection) String() string { return proto.CompactTextString(m) }
func (*Connection) ProtoMessage()    {}
func (*Connection) Descriptor() ([]byte, []int) {
	return fileDescriptor_36fc7553ab6b549b, []int{0}
}

func (m *Connection) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Connection.Unmarshal(m, b)
}
func (m *Connection) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Connection.Marshal(b, m, deterministic)
}
func (m *Connection) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Connection.Merge(m, src)
}
func (m *Connection) XXX_Size() int {
	return xxx_messageInfo_Connection.Size(m)
}
func (m *Connection) XXX_DiscardUnknown() {
	xxx_messageInfo_Connection.DiscardUnknown(m)
}

var xxx_messageInfo_Connection proto.InternalMessageInfo

func (m *Connection) GetProtocol() Connection_Protocol {
	if m != nil {
		return m.Protocol
	}
	return Connection_UNKNOWN
}

func (m *Connection) GetSrcIp() string {
	if m != nil {
		return m.SrcIp
	}
	return ""
}

func (m *Connection) GetSrcPort() uint32 {
	if m != nil {
		return m.SrcPort
	}
	return 0
}

func (m *Connection) GetDstIp() string {
	if m != nil {
		return m.DstIp
	}
	return ""
}

func (m *Connection) GetDstHost() string {
	if m != nil {
		return m.DstHost
	}
	return ""
}

func (m *Connection) GetDstPort() uint32 {
	if m != nil {
		return m.DstPort
	}
	return 0
}

func (m *Connection) GetUserId() uint32 {
	if m != nil {
		return m.UserId
	}
	return 0
}

func (m *Connection) GetProcessId() uint32 {
	if m != nil {
		return m.ProcessId
	}
	return 0
}

func (m *Connection) GetProcessPath() string {
	if m != nil {
		return m.ProcessPath
	}
	return ""
}

func (m *Connection) GetProcessArgs() []string {
	if m != nil {
		return m.ProcessArgs
	}
	return nil
}

func init() {
	proto.RegisterEnum("opensnitch.network.Connection_Protocol", Connection_Protocol_name, Connection_Protocol_value)
	proto.RegisterType((*Connection)(nil), "opensnitch.network.Connection")
}

func init() { proto.RegisterFile("opensnitch/network/network.proto", fileDescriptor_36fc7553ab6b549b) }

var fileDescriptor_36fc7553ab6b549b = []byte{
	// 333 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x64, 0x91, 0x41, 0x4b, 0xf3, 0x40,
	0x10, 0x86, 0xbf, 0xb4, 0x5f, 0x93, 0x74, 0xab, 0x52, 0x16, 0xc4, 0x78, 0x10, 0x62, 0x2f, 0xd6,
	0x43, 0x53, 0xa8, 0xfe, 0x01, 0xad, 0x07, 0x8b, 0x12, 0x43, 0xb1, 0x08, 0x5e, 0x4a, 0xbb, 0x59,
	0x92, 0x60, 0xdd, 0x09, 0x33, 0x53, 0xfc, 0xed, 0xde, 0x24, 0xdb, 0xc4, 0x16, 0x3c, 0x25, 0xfb,
	0x3e, 0xef, 0x33, 0x0b, 0xb3, 0x22, 0x84, 0x52, 0x1b, 0x32, 0x05, 0xab, 0x7c, 0x6c, 0x34, 0x7f,
	0x01, 0x7e, 0x34, 0xdf, 0xa8, 0x44, 0x60, 0x90, 0x72, 0xdf, 0x88, 0x6a, 0x32, 0xf8, 0x6e, 0x09,
	0x31, 0x05, 0x63, 0xb4, 0xe2, 0x02, 0x8c, 0x9c, 0x0a, 0xdf, 0x76, 0x15, 0x6c, 0x02, 0x27, 0x74,
	0x86, 0x27, 0x93, 0xab, 0xe8, 0xaf, 0x15, 0xed, 0x8d, 0x28, 0xa9, 0xeb, 0xf3, 0x5f, 0x51, 0x9e,
	0x0a, 0x97, 0x50, 0x2d, 0x8b, 0x32, 0x68, 0x85, 0xce, 0xb0, 0x3b, 0xef, 0x10, 0xaa, 0x59, 0x29,
	0xcf, 0x85, 0x5f, 0xc5, 0x25, 0x20, 0x07, 0xed, 0xd0, 0x19, 0x1e, 0xcf, 0x3d, 0x42, 0x95, 0x00,
	0x72, 0x65, 0xa4, 0xc4, 0x95, 0xf1, 0x7f, 0x67, 0xa4, 0xc4, 0x3b, 0xa3, 0x8a, 0x73, 0x20, 0x0e,
	0x3a, 0x16, 0x78, 0x29, 0xf1, 0x23, 0x10, 0x37, 0xc8, 0x0e, 0x73, 0x77, 0xc3, 0x52, 0x62, 0x3b,
	0xec, 0x4c, 0x78, 0x5b, 0xd2, 0xb8, 0x2c, 0xd2, 0xc0, 0xb3, 0xc4, 0xad, 0x8e, 0xb3, 0x54, 0x5e,
	0x08, 0x51, 0x22, 0x28, 0x4d, 0x54, 0x31, 0xdf, 0xb2, 0x6e, 0x9d, 0xcc, 0x52, 0x79, 0x29, 0x8e,
	0x1a, 0x5c, 0xae, 0x38, 0x0f, 0xba, 0xf6, 0xc6, 0x5e, 0x9d, 0x25, 0x2b, 0xce, 0x0f, 0x2b, 0x2b,
	0xcc, 0x28, 0x10, 0x61, 0xfb, 0xa0, 0x72, 0x87, 0x19, 0x0d, 0xae, 0x85, 0xdf, 0xac, 0x44, 0xf6,
	0x84, 0xb7, 0x88, 0x9f, 0xe2, 0x97, 0xb7, 0xb8, 0xff, 0x4f, 0x7a, 0xa2, 0xfd, 0x3a, 0x4d, 0xfa,
	0x4e, 0xf5, 0xb3, 0x78, 0x48, 0xfa, 0xad, 0xfb, 0xdb, 0xf7, 0x49, 0x56, 0x70, 0xbe, 0x5d, 0x47,
	0x0a, 0x3e, 0xc7, 0x31, 0x20, 0xe7, 0x1a, 0xcd, 0xe8, 0xb9, 0xc8, 0x72, 0xa6, 0x31, 0xd0, 0x08,
	0xb7, 0x1b, 0x4d, 0x23, 0x6d, 0xb2, 0xc2, 0xe8, 0xe6, 0x2d, 0xd7, 0xae, 0xdd, 0xf3, 0xcd, 0x4f,
	0x00, 0x00, 0x00, 0xff, 0xff, 0x29, 0x71, 0x6e, 0xd6, 0xf0, 0x01, 0x00, 0x00,
}
