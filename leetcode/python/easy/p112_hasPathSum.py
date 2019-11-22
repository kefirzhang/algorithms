# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum_num):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum_num:
            return True

        if self.hasPathSum(root.left, sum_num - root.val):
            return True
        if self.hasPathSum(root.right, sum_num - root.val):
            return True

        return False


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(4)
slu = Solution()
print(slu.hasPathSum(p, 4))
