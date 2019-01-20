package engine

import (
	"fmt"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

// An Expression can evaluate whether a connection matches
type Expression interface {
	Evaluate(*network.Connection) bool
}

// ExpressionSerializer is an Expression that can be serialized into a
// protocol buffer Expression
type ExpressionSerializer interface {
	Expression
	Serializer
}

// A Serializer can be serialized into a protocol buffer Expression
type Serializer interface {
	Serialize() *rules.Expression
}

// Deserialize attempts to take an Expression protocol buffer and deserialize it
// into an evaluable (and serializable) expression
func Deserialize(x *rules.Expression) (expr ExpressionSerializer, err error) {
	if x == nil {
		err = fmt.Errorf("engine: cannot deserialize a nil expression")
		return
	}

	switch x.Operation {
	case rules.Operation_AND:
		expr, err = deserializeAnd(x)

	case rules.Operation_OR:
		expr, err = deserializeOr(x)

	case rules.Operation_NOT:
		expr, err = deserializeNot(x)

	case rules.Operation_DST_IP:
		expr, err = deserializeStrExpression(x)

	case rules.Operation_DST_HOST:
		expr, err = deserializeHost(x)

	case rules.Operation_DST_PORT:
		expr, err = deserializePort(x)

	case rules.Operation_PROC_PATH:
		expr, err = deserializeProcPath(x)

	case rules.Operation_PID:
		expr, err = deserializePID(x)

	default:
		err = fmt.Errorf("engine: can't deserialize expression w/ operand %d", x.Operation)
	}

	return
}
