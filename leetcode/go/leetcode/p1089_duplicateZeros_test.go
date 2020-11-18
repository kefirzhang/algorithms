package leetcode

import (
	"fmt"
	"reflect"
	"testing"
)

func TestDuplicateZeros(t *testing.T) {
	var TestCases = []struct {
		in       []int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
		{[]int{0, 0, 0, 0, 0}, []int{0, 0, 0, 0, 0}},
		{[]int{1, 2, 3, 0, 5}, []int{1, 2, 3, 0, 0}},
		{[]int{0, 2, 0, 4, 5}, []int{0, 0, 2, 0, 0}},
	}

	for _, tc := range TestCases {
		fmt.Printf("In%v", tc.in)
		duplicateZeros(tc.in)
		fmt.Printf("Out%v", tc.in)

		if !reflect.DeepEqual(tc.expected, tc.in) {
			fmt.Printf("Fail %v\n", tc.expected)
		} else {
			fmt.Printf("Success %v\n", tc.expected)
		}
	}
}
