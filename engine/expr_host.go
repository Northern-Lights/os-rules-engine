package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

type host string

func (x host) Evaluate(c *network.Connection) bool {
	return c.DstHost == string(x)
}

func (x host) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_DST_HOST,
		Strings:   []string{string(x)},
	}
}

// Host returns an expression that evaluates to true if the connection's
// destination host matches the given hostname
func Host(hostname string) ExpressionSerializer {
	return host(hostname)
}

func deserializeHost(x *rules.Expression) (expr ExpressionSerializer, err error) {
	if len(x.Strings) < 1 {
		err = fmt.Errorf(`engine: no string operands to parse hostname`)
		return
	}

	hostname := x.Strings[0]

	expr = Host(hostname)
	return
}
