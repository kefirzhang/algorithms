# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def helper(node, value):
            if not node:
                return 0
            res = 0
            if node.val == value:
                res += 1
            value -= node.val
            return res + helper(node.left, value) + helper(node.right, value)
        if not root:
            return 0
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.right.right = TreeNode(4)
tree.right.right.right.right = TreeNode(5)

slu = Solution()
print(slu.pathSum(tree, 3))
