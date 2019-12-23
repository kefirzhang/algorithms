# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        return 10


slu = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.right = TreeNode(3)
t1.right.right = TreeNode(1)
