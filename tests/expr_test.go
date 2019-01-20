package tests

import (
	"testing"

	"github.com/Northern-Lights/os-rules-engine/engine"
	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

var conn = &network.Connection{
	DstIp:       "192.168.1.1",
	DstPort:     53,
	ProcessId:   9741,
	ProcessPath: "/usr/bin/firefox",
	UserId:      501,
}

func TestTrueExpression(t *testing.T) {
	var (
		condition *rules.Expression
		condIP    *rules.Expression
		condPort  *rules.Expression
	)

	condIP = &rules.Expression{
		Operation: rules.Operation_DST_IP,
		Strings:   []string{"192.168.1.1"},
	}

	condPort = &rules.Expression{
		Operation: rules.Operation_DST_PORT,
		Uint32S:   []uint32{53},
	}

	condition = &rules.Expression{
		Operation: rules.Operation_AND,
		Left:      condIP,
		Right:     condPort,
	}

	expr, err := engine.Deserialize(condition)
	if err != nil {
		t.Fatalf("Couldn't deserialize rule: %s", err)
	}

	result := expr.Evaluate(conn)
	if result == false {
		t.Fatalf("Result was false; should have been true")
	}
}

func TestFalseExpression(t *testing.T) {
	var (
		condition *rules.Expression
		condIP    *rules.Expression
		condPort  *rules.Expression
	)

	condIP = &rules.Expression{
		Operation: rules.Operation_DST_IP,
		Strings:   []string{"192.168.1.10"},
	}

	condPort = &rules.Expression{
		Operation: rules.Operation_DST_PORT,
		Uint32S:   []uint32{53},
	}

	condition = &rules.Expression{
		Operation: rules.Operation_AND,
		Left:      condIP,
		Right:     condPort,
	}

	expr, err := engine.Deserialize(condition)
	if err != nil {
		t.Fatalf("Couldn't deserialize rule: %s", err)
	}

	result := expr.Evaluate(conn)
	if result == true {
		t.Fatalf("Result was true; should have been false")
	}
}

func TestSerializeDeserialize(t *testing.T) {
	var (
		ip       = "192.168.1.1"
		port     = uint32(53)
		condIP   = engine.IPAddr(ip)
		condPort = engine.Port(port)
	)

	condition := engine.And(condIP, condPort)
	result1 := condition.Evaluate(conn)
	if result1 != true {
		t.Fatalf("Resulted in true; expected false")
	}

	serialized := condition.Serialize()
	if serialized.Operation != rules.Operation_AND {
		t.Fatalf("Expected %s; got %s", rules.Operation_AND, serialized.Operation)
	}
	if serialized.Left == nil {
		t.Fatalf("No left expression")
	}
	if serialized.Right == nil {
		t.Fatalf("No right expression")
	}
	if serialized.Left.Operation != rules.Operation_DST_IP || len(serialized.Left.Strings) == 0 {
		t.Errorf("Left expression wrong operation or missing operand")
	}
	if serialized.Right.Operation != rules.Operation_DST_PORT || len(serialized.Right.Uint32S) == 0 {
		t.Errorf("Right expression wrong operation or missing operand")
	}
}
