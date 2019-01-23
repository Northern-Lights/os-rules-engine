package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
	"github.com/evilsocket/opensnitch/daemon/rule"
)

type pid uint32

func (x pid) Evaluate(c *network.Connection) bool {
	return c.ProcessId == uint32(x)
}

func (x pid) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_PID,
		Uint32S:   []uint32{uint32(x)},
	}
}

// PID returns an expression that evaluates to true if the connection's
// process's pid matches the given pid
func PID(n uint32) rule.ExpressionSerializer {
	return pid(n)
}

func deserializePID(x *rules.Expression) (expr rule.ExpressionSerializer, err error) {
	if len(x.Uint32S) < 1 {
		err = fmt.Errorf(`engine: no uint32 operands to parse pid`)
		return
	}

	pidNum := x.Uint32S[0]

	expr = PID(pidNum)
	return
}
