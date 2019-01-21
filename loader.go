package engine

import (
	"encoding/json"
	"io"

	"github.com/Northern-Lights/os-rules-engine/rules"
)

// JSONLoader can load and store rules
type JSONLoader struct {
	rulesFilePath string
}

// LoadRules loads JSON-formatted rules
func (ldr *JSONLoader) LoadRules(r io.Reader) ([]*rules.Rule, error) {
	out := make([]*rules.Rule, 0, 500)
	dec := json.NewDecoder(r)
	err := dec.Decode(&out)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SaveRules saves rules as JSON-formatted data
func (ldr *JSONLoader) SaveRules(w io.Writer, r []*rules.Rule) error {
	enc := json.NewEncoder(w)
	err := enc.Encode(&r)
	if err != nil {
		return err
	}

	return nil
}
