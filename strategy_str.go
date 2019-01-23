// Algorithms for comparing string types

package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/rules"
	"github.com/evilsocket/opensnitch/daemon/rule"
)

type strCmp func(target, comparison string) bool

func strEquals(target, comparison string) bool {
	return target == comparison
}

type strExpression struct {
	op         rules.Operation
	comparison string
	cmp        strCmp
}

func (s strExpression) Evaluate(target string) bool {
	return s.cmp(target, s.comparison)
}

func (s strExpression) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: s.op,
		Strings:   []string{s.comparison},
	}
}

func deserializeStrExpression(x *rules.Expression) (expr rule.ExpressionSerializer, err error) {
	if len(x.Strings) < 1 {
		err = fmt.Errorf(`engine: no string operands to parse %s`, x.Operation)
		return
	}

	switch x.Operation {
	case rules.Operation_DST_IP:
		expr = IPAddr(x.Strings[0])

	case rules.Operation_DST_HOST:
		expr = Host(x.Strings[0])

	case rules.Operation_PROC_PATH:
		expr = ProcPath(x.Strings[0])

	default:
		err = fmt.Errorf(`engine: no deserialization for string expression %s`, x.Operation)
	}

	return
}
