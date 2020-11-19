package leetcode

func convertBiNode(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	if root.Left == nil && root.Right == nil {
		return root
	}
	if root.Left == nil {
		root.Right = convertBiNode(root.Right)
		return root
	}
	left := convertBiNode(root.Left)
	root.Right = convertBiNode(root.Right)
	root.Left = nil
	lastNode := left

	for lastNode.Right != nil {
		lastNode = lastNode.Right
	}
	lastNode.Right = root
	return left
}
