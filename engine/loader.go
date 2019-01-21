package engine

import (
	"encoding/json"
	"io"

	"github.com/Northern-Lights/os-rules-engine/rules"
)

// RuleLoadSaver can load and store rules
type RuleLoadSaver interface {
	RuleLoader
	RuleSaver
}

// A RuleLoader loads rules from a reader source
type RuleLoader interface {
	LoadRules(io.Reader) ([]*Rule, error)
}

// A RuleSaver saves rules to a storage writer
type RuleSaver interface {
	SaveRules(io.Writer, []*Rule) error
}

// JSONLoader can load and store rules
type JSONLoader struct{}

// LoadRules loads JSON-formatted rules
func (ldr *JSONLoader) LoadRules(r io.Reader) ([]*Rule, error) {
	out := make([]*Rule, 0, 500)
	dec := json.NewDecoder(r)
	err := dec.Decode(&out)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SaveRules saves rules as JSON-formatted data
func (ldr *JSONLoader) SaveRules(w io.Writer, r []*Rule) error {
	pbFmt := make([]*rules.Rule, len(r))
	for i := range r {
		pbFmt[i] = r[i].Rule
	}

	enc := json.NewEncoder(w)
	err := enc.Encode(&pbFmt)
	if err != nil {
		return err
	}

	return nil
}
