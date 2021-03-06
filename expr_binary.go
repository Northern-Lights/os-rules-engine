/*
 * TRUE, FALSE, AND, OR, NOT
 * - Evaluation
 * - Serialization
 * - Deserialization
 */

package engine

import (
	"fmt"

	"github.com/evilsocket/opensnitch/network"
	"github.com/evilsocket/opensnitch/rules"
)

type boolExpr struct {
	op rules.Operation
}

func (x boolExpr) Evaluate(_ *network.Connection) bool {
	return x.op == rules.Operation_TRUE
}

func (x boolExpr) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: x.op,
	}
}

// Bool returns an EvaluatorSerializer which will return the value given,
// regardless of the connection to be verified against. Useful for
// short-circuiting other expressions
func Bool(value bool) rules.EvaluatorSerializer {
	var x boolExpr
	if value == true {
		x.op = rules.Operation_TRUE
	} else {
		x.op = rules.Operation_FALSE
	}
	return x
}

func deserializeBool(x *rules.Expression) (expr rules.EvaluatorSerializer, err error) {
	expr = boolExpr{
		op: x.Operation,
	}
	return
}

type binaryEvaluatorConstructor func(x1, x2 rules.EvaluatorSerializer) rules.EvaluatorSerializer

func buildBinaryEvaluator(x *rules.Expression, op rules.Operation, bec binaryEvaluatorConstructor) (expr rules.EvaluatorSerializer, err error) {
	if x.Operation != op {
		err = fmt.Errorf(`engine: expected operation %s; got %s`, op, x.Operation)
		return
	}

	if x.Left == nil {
		err = fmt.Errorf(`engine: nil left operand for %s operator`, x.Operation)
		return
	}
	left, err := Deserialize(x.Left)
	if err != nil {
		return
	}

	if x.Right == nil {
		err = fmt.Errorf(`engine: nil right operand for %s operator`, x.Operation)
		return
	}
	right, err := Deserialize(x.Right)
	if err != nil {
		return
	}

	expr = bec(left, right)
	return
}

type and struct {
	op    rules.Operation
	left  rules.EvaluatorSerializer
	right rules.EvaluatorSerializer
}

func (x and) Evaluate(c *network.Connection) bool {
	return x.left.Evaluate(c) && x.right.Evaluate(c)
}

func (x and) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_AND,
		Left:      x.left.Serialize(),
		Right:     x.right.Serialize(),
	}
}

func And(x1, x2 rules.EvaluatorSerializer) rules.EvaluatorSerializer {
	return &and{
		op:    rules.Operation_AND,
		left:  x1,
		right: x2,
	}
}

func deserializeAnd(x *rules.Expression) (expr rules.EvaluatorSerializer, err error) {
	expr, err = buildBinaryEvaluator(x, rules.Operation_AND, And)
	return
}

type or struct {
	op    rules.Operation
	left  rules.EvaluatorSerializer
	right rules.EvaluatorSerializer
}

func (x or) Evaluate(c *network.Connection) bool {
	return x.left.Evaluate(c) || x.right.Evaluate(c)
}

func (x or) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_OR,
		Left:      x.left.Serialize(),
		Right:     x.right.Serialize(),
	}
}

func Or(x1, x2 rules.EvaluatorSerializer) rules.EvaluatorSerializer {
	return &or{
		op:    rules.Operation_OR,
		left:  x1,
		right: x2,
	}
}

func deserializeOr(x *rules.Expression) (expr rules.EvaluatorSerializer, err error) {
	expr, err = buildBinaryEvaluator(x, rules.Operation_OR, Or)
	return
}

type not struct {
	op   rules.Operation
	left rules.EvaluatorSerializer
}

func (x not) Evaluate(c *network.Connection) bool {
	return !x.left.Evaluate(c)
}

func (x not) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_NOT,
		Left:      x.left.Serialize(),
	}
}

func Not(x1 rules.EvaluatorSerializer) rules.EvaluatorSerializer {
	return &not{
		op:   rules.Operation_NOT,
		left: x1,
	}
}

func deserializeNot(x *rules.Expression) (expr rules.EvaluatorSerializer, err error) {
	if x.Operation != rules.Operation_NOT {
		err = fmt.Errorf(`engine: expected operation %s; got %s`, rules.Operation_NOT, x.Operation)
		return
	}

	if x.Left == nil {
		err = fmt.Errorf(`engine: nil left operand for %s operator`, x.Operation)
		return
	}
	left, err := Deserialize(x.Left)
	if err != nil {
		return
	}

	expr = Not(left)
	return
}
