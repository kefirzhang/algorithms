# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root, depth=0):
        if root is None:
            return depth

        if root.left is not None and root.right is not None:
            return min(self.minDepth(root.left, depth), self.minDepth(root.right, depth)) + 1

        if root.left is None:
            return self.minDepth(root.right, depth) + 1
        if root.right is None:
            return self.minDepth(root.left, depth) + 1



#  [1,2,3,4,null,null,5]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(4)
slu = Solution()
print(slu.minDepth(p))
