package leetcode

import (
	"fmt"
	"testing"
)

func TestCheckSubarraySum(t *testing.T) {
	var TestCases = []struct {
		inArr  []int
		inNum  int
		expect bool
	}{
		{[]int{1, 2, 3, 4, 5, 6}, 7, true},
		{[]int{1, 2, 3, 4, 5, 6}, 12, true},
		{[]int{1}, 7, false},
		{[]int{1, 2, 3, 4, 5, 6}, 11, true},
		{[]int{0}, 0, false},
		{[]int{0, 0}, 0, true},
	}

	for _, tc := range TestCases {
		out := checkSubarraySum(tc.inArr, tc.inNum)
		if out == tc.expect {
			fmt.Printf("Pass: inArr:%v inNum:%v out:%v expect:%v\r\n", tc.inArr, tc.inArr, out, tc.expect)
		} else {
			fmt.Printf("Fail: inArr:%v inNum:%v out:%v expect:%v\r\n", tc.inArr, tc.inArr, out, tc.expect)
		}
	}
}
