# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这里存在重复计算的问题 可以优化
class Solution:
    def getHigh(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.getHigh(root.right) + 1
        if root.right is None:
            return self.getHigh(root.left) + 1

        return max(self.getHigh(root.right), self.getHigh(root.left)) + 1

    def isBalanced(self, root):
        if root is None:
            return True
        h_left = self.getHigh(root.left)
        h_right = self.getHigh(root.right)
        if abs(h_left - h_right) > 1:
            return False

        if self.isBalanced(root.left) is False:
            return False
        if self.isBalanced(root.right) is False:
            return False

        return True


# [1,2,2,3,null,null,3,4,null,null,4]
p = TreeNode(1)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)
slu = Solution()
print(slu.isBalanced(p))
