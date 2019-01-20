package engine

import (
	"fmt"
	"net"

	"github.com/Northern-Lights/os-rules-engine/network"
	"github.com/Northern-Lights/os-rules-engine/rules"
)

type ipAddr string

func (x ipAddr) Evaluate(c *network.Connection) bool {
	return c.DstIp == string(x)
}

func (x ipAddr) Serialize() *rules.Expression {
	return &rules.Expression{
		Operation: rules.Operation_DST_IP,
		Strings:   []string{string(x)},
	}
}

// IPAddr returns an expression that evaluates to true if the connection's
// destination IP address matches the given address
func IPAddr(addr string) ExpressionSerializer {
	return ipAddr(addr)
}

func deserializeIPAddr(x *rules.Expression) (expr ExpressionSerializer, err error) {
	if len(x.Strings) < 1 {
		err = fmt.Errorf(`engine: no string operands to parse IP`)
		return
	}
	ipString := x.Strings[0]
	ip := net.ParseIP(ipString)
	if ip == nil {
		err = fmt.Errorf(`engine: invalid IP address "%s"`, ip)
		return
	}

	expr = IPAddr(ipString)
	return
}
