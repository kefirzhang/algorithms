package leetcode

import (
	"fmt"
	"testing"
)

func TestLongestUnivaluePath(t *testing.T) {
	node := TreeNode{5, nil, nil}
	node.Left = &TreeNode{5, nil, nil}
	node.Right = &TreeNode{5, nil, nil}
	var TestCases = []struct {
		node TreeNode
		path int
	}{
		{node, 2},
	}
	for _, tc := range TestCases {
		if longestUnivaluePath(&tc.node) == tc.path {
			fmt.Printf("Pass TreeNode:%v path:%v \r\n", tc.node, tc.path)
		} else {
			fmt.Printf("Fail TreeNode:%v path:%v \r\n", tc.node, tc.path)
		}
	}
}
