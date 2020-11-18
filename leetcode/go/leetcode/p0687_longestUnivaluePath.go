package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestUnivaluePath(root *TreeNode) int {
	var max func(i, n int) int
	max = func(i, n int) int {
		if i > n {
			return i
		}
		return n
	}
	ans := 0
	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left) + 1
		right := dfs(node.Right) + 1
		if node.Left == nil || node.Val != node.Left.Val {
			left = 0
		}
		if node.Right == nil || node.Val != node.Right.Val {
			right = 0
		}
		ans = max(ans, right+left)
		return max(left, right)
	}
	dfs(root)
	return ans
}
