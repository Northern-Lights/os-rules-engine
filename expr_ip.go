package engine

import (
	"github.com/evilsocket/opensnitch/network"
	"github.com/evilsocket/opensnitch/rules"
)

type ipAddr struct {
	strExpression
}

func (x ipAddr) Evaluate(c *network.Connection) bool {
	return x.strExpression.Evaluate(c.DstIp)
}

// IPAddr returns an expression that evaluates to true if the connection's
// destination IP address matches the given address
func IPAddr(addr string) rules.EvaluatorSerializer {
	return ipAddr{
		strExpression{
			op:         rules.Operation_DST_IP,
			comparison: addr,
			cmp:        strEquals,
		},
	}
}
