package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

type port uint32

func (x port) Evaluate(c *network.Connection) bool {
	return c.DstPort == uint32(x)
}

func (x port) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_DST_PORT,
		Uint32S:   []uint32{uint32(x)},
	}
}

// Port returns an expression that evaluates to true if the connection's
// destination port matches the given port
func Port(portnum uint32) ExpressionSerializer {
	return port(portnum)
}

func deserializePort(x *rules.Expression) (expr ExpressionSerializer, err error) {
	if len(x.Uint32S) < 1 {
		err = fmt.Errorf(`engine: no uint32 operands to parse port`)
		return
	}

	portnum := x.Uint32S[0]

	expr = Port(portnum)
	return
}
