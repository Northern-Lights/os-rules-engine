package engine

import (
	"github.com/evilsocket/opensnitch/network"
	"github.com/evilsocket/opensnitch/rules"
)

type procPath struct {
	strExpression
}

func (x procPath) Evaluate(c *network.Connection) bool {
	return x.strExpression.Evaluate(c.ProcessPath)
}

// ProcPath returns an expression that evaluates to true if the connection's
// process path matches the given process path
func ProcPath(pp string) rules.EvaluatorSerializer {
	return &procPath{
		strExpression{
			op:         rules.Operation_PROC_PATH,
			comparison: pp,
			cmp:        strEquals,
		},
	}
}
