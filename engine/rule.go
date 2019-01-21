package engine

import (
	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

// A Rule can be evaluated directly
type Rule struct {
	*rules.Rule
}

// Evaluate ...
func (r Rule) Evaluate(c *network.Connection) bool {
	condition, err := Deserialize(r.Condition)
	if err != nil {
		return false
	}
	return condition.Evaluate(c)
}

// NewRule initializes a Rule with a rules.Rule
func NewRule(a rules.Action, d rules.Duration, condition ExpressionSerializer) *Rule {
	return &Rule{
		&rules.Rule{
			Action:    a,
			Duration:  d,
			Condition: condition.Serialize(),
		},
	}
}
