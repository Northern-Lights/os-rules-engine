package tests

import (
	"io"
	"io/ioutil"
	"testing"

	engine "github.com/Northern-Lights/os-rules-engine"
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

var localhostDNSRule = &rules.Rule{
	Action:   rules.Action_ALLOW,
	Duration: rules.Duration_FIREWALL_SESSION,
	Condition: &rules.Expression{
		Operation: rules.Operation_AND,
		Left: &rules.Expression{
			Operation: rules.Operation_DST_HOST,
			Strings:   []string{"127.0.0.1"},
		},
		Right: &rules.Expression{
			Operation: rules.Operation_DST_PORT,
			Uint32S:   []uint32{53},
		},
	},
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

func TestShortCircuitTrue(t *testing.T) {
	var (
		wrongIP   = "10.1.1.1"
		wrongPort = uint32(99)
		condIP    = engine.IPAddr(wrongIP)
		condPort  = engine.Port(wrongPort)
		condWrong = engine.And(condIP, condPort)
	)

	matched := condWrong.Evaluate(conn)
	if matched {
		t.Fatalf(`Wrong condition somehow matched`)
	}

	condTrue := engine.Bool(true)
	shortCircuitTrue := engine.Or(condTrue, condWrong)
	matched = shortCircuitTrue.Evaluate(conn)
	if !matched {
		t.Errorf(`Wrong condition was not short circuited`)
	}
}

func TestPersistence(t *testing.T) {
	f, err := ioutil.TempFile("", "os-rules-engine-test")
	if err != nil {
		t.Fatalf("Couldn't create temp file: %s", err)
	}

	rule := localhostDNSRule

	var ldr engine.JSONLoader
	err = ldr.SaveRules(f, []*rules.Rule{rule})
	if err != nil {
		t.Fatalf(`Couldn't save rule: %s`, err)
	}

	err = f.Sync()
	if err != nil {
		t.Fatalf(`Couldn't flush file: %s`, err)
	}

	_, err = f.Seek(0, io.SeekStart)
	if err != nil {
		t.Fatalf(`Couldn't rewind file: %s`, err)
	}

	loadedRules, err := ldr.LoadRules(f)
	if err != nil {
		t.Fatalf(`Couldn't load rules: %s`, err)
	}
	if len(loadedRules) < 1 {
		t.Fatalf(`No rules in loaded ruleset`)
	}

	loadedRule := loadedRules[0]
	if loadedRule.Action != localhostDNSRule.Action {
		t.Errorf("Expected action %s; got %s",
			localhostDNSRule.Action,
			loadedRule.Action)
	}
	if loadedRule.Duration != localhostDNSRule.Duration {
		t.Errorf("Expected duration %s; got %s",
			localhostDNSRule.Duration,
			loadedRule.Duration)
	}
	if loadedRule.Condition.Operation != localhostDNSRule.Condition.Operation {
		t.Errorf("Expected 1st level condition %s; got %s",
			localhostDNSRule.Condition.Operation,
			loadedRule.Condition.Operation)
	}
}
