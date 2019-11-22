# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, p, d=0):
        if p is None:
            return 0
        d = d + 1
        d_left = self.maxDepth(p.left, d)
        d_right = self.maxDepth(p.right, d)

        return max(d, d_left, d_right)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(4)
slu = Solution()
print(slu.maxDepth(p))
