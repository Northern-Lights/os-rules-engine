package engine

import (
	"encoding/json"
	"os"
	"sync"

	"github.com/Northern-Lights/os-rules-engine/rules"
)

// JSONLoader can load and store rules
type JSONLoader struct {
	sync.RWMutex

	rulesFilePath string
}

func NewJSONLoader(rulesFilePath string) *JSONLoader {
	return &JSONLoader{
		rulesFilePath: rulesFilePath,
	}
}

// LoadRules loads JSON-formatted rules. No error occurs if file doesn't exist
func (ldr *JSONLoader) LoadRules() ([]*rules.Rule, error) {
	ldr.RLock()
	defer ldr.RUnlock()

	f, err := os.Open(ldr.rulesFilePath)
	if os.IsNotExist(err) {
		return []*rules.Rule{}, nil
	}
	if err != nil {
		return nil, err
	}
	defer f.Close()

	out := make([]*rules.Rule, 0, 500)
	dec := json.NewDecoder(f)
	err = dec.Decode(&out)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SaveRules saves rules as JSON-formatted data
func (ldr *JSONLoader) SaveRules(r []*rules.Rule) error {
	ldr.Lock()
	defer ldr.Unlock()

	f, err := os.Create(ldr.rulesFilePath)
	if err != nil {
		return err
	}
	defer f.Close()

	enc := json.NewEncoder(f)
	err = enc.Encode(&r)
	if err != nil {
		return err
	}

	return nil
}
