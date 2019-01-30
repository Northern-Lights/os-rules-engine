package engine

import (
	"fmt"

	"github.com/evilsocket/opensnitch/rules"
)

// Deserialize attempts to take an Expression protocol buffer and deserialize it
// into an EvaluatorSerializer
func Deserialize(x *rules.Expression) (expr rules.EvaluatorSerializer, err error) {
	if x == nil {
		err = fmt.Errorf("engine: cannot deserialize a nil expression")
		return
	}

	switch x.Operation {
	case rules.Operation_TRUE:
		expr, err = deserializeBool(x)

	case rules.Operation_FALSE:
		expr, err = deserializeBool(x)

	case rules.Operation_AND:
		expr, err = deserializeAnd(x)

	case rules.Operation_OR:
		expr, err = deserializeOr(x)

	case rules.Operation_NOT:
		expr, err = deserializeNot(x)

	case rules.Operation_DST_IP:
		expr, err = deserializeStrExpression(x)

	case rules.Operation_DST_HOST:
		expr, err = deserializeStrExpression(x)

	case rules.Operation_DST_PORT:
		expr, err = deserializePort(x)

	case rules.Operation_PROC_PATH:
		expr, err = deserializeStrExpression(x)

	case rules.Operation_PID:
		expr, err = deserializePID(x)

	default:
		err = fmt.Errorf("engine: can't deserialize expression w/ operand %d", x.Operation)
	}

	return
}
