package leetcode

import (
	"fmt"
	"testing"
)

func TestReachNumber(t *testing.T) {
	var TestCases = []struct {
		in     int
		expect int
	}{
		//{20, 4},
		{3, 2},
		{2, 3},
		{-2, 3},
	}
	for _, tc := range TestCases {
		out := reachNumber(tc.in)
		if out == tc.expect {
			fmt.Printf("Pass in:%v,out:%v expect:%v \r\n", tc.in, out, tc.expect)
		} else {
			fmt.Printf("Fail in:%v,out:%v expect:%v \r\n", tc.in, out, tc.expect)
		}
	}
}
