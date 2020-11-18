package leetcode

import (
	"fmt"
	"reflect"
	"testing"
)

func TestAddToArrayForm(t *testing.T) {

	var TestCases = []struct {
		in1      []int
		in2      int
		expected []int
	}{
		{[]int{1, 2, 3, 4, 5}, 10, []int{1, 2, 3, 5, 5}},
		{[]int{1, 2, 3, 4, 5}, 100000, []int{1, 1, 2, 3, 4, 5}},
		{[]int{2, 1, 5}, 806, []int{1, 0, 2, 1}},
	}

	for _, tc := range TestCases {
		back := addToArrayForm(tc.in1, tc.in2)
		if !reflect.DeepEqual(back, tc.expected) {
			t.Errorf("in1:%d in2:%v out:%v expected:%v\r\n", tc.in1, tc.in2, back, tc.expected)
		} else {
			fmt.Printf("Succes in1:%v in2:%v out:%v expected:%v\r\n", tc.in1, tc.in2, back, tc.expected)
		}
	}

}
