package engine

import (
	"github.com/evilsocket/opensnitch/network"
	"github.com/evilsocket/opensnitch/rules"
)

type host struct {
	strExpression
}

func (x host) Evaluate(c *network.Connection) bool {
	return x.strExpression.Evaluate(c.DstHost)
}

// Host returns an expression that evaluates to true if the connection's
// destination host matches the given hostname
func Host(hostname string) rules.EvaluatorSerializer {
	return &host{
		strExpression{
			op:         rules.Operation_DST_HOST,
			comparison: hostname,
			cmp:        strEquals,
		},
	}
}
