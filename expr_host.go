package engine

import (
	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
	"github.com/evilsocket/opensnitch/daemon/rule"
)

type host struct {
	strExpression
}

func (x host) Evaluate(c *network.Connection) bool {
	return x.strExpression.Evaluate(c.DstHost)
}

// Host returns an expression that evaluates to true if the connection's
// destination host matches the given hostname
func Host(hostname string) rule.ExpressionSerializer {
	return &host{
		strExpression{
			op:         rules.Operation_DST_HOST,
			comparison: hostname,
			cmp:        strEquals,
		},
	}
}
