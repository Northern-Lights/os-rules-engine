package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

type procPath string

func (x procPath) Evaluate(c *network.Connection) bool {
	return c.DstIp == string(x)
}

func (x procPath) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_PROC_PATH,
		Strings:   []string{string(x)},
	}
}

// ProcPath returns an expression that evaluates to true if the connection's
// process path matches the given process path
func ProcPath(pp string) ExpressionSerializer {
	return procPath(pp)
}

func deserializeProcPath(x *rules.Expression) (expr ExpressionSerializer, err error) {
	if len(x.Strings) < 1 {
		err = fmt.Errorf(`engine: no string operands to parse process path`)
		return
	}

	pathString := x.Strings[0]
	if pathString == "" {
		err = fmt.Errorf(`engine: empty string used as process path`)
		return
	}

	expr = ProcPath(pathString)
	return
}
