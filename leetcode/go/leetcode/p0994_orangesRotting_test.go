package leetcode

import (
	"fmt"
	"testing"
)

func TestOrangesRotting(t *testing.T) {
	var TestCases = []struct {
		in     [][]int
		expect int
	}{
		{[][]int{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}, 4},
		{[][]int{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}}, -1},
	}
	for _, tc := range TestCases {
		re := orangesRotting(tc.in)
		if re == tc.expect {
			fmt.Printf("Success in:%v expect:%v result:%v\r\n", tc.in, tc.expect, re)
		} else {
			fmt.Printf("Fail in:%v expect:%v result:%v\r\n", tc.in, tc.expect, re)
		}
	}
}
