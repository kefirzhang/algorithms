# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.right is None and root.left is None:
            return True
        return self.isSymmetricSameTree(root.left, root.right)

    def isSymmetricSameTree(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        if left.val != right.val:
            return False

        b_left = self.isSymmetricSameTree(left.left, right.right)
        b_right = self.isSymmetricSameTree(left.right, right.left)

        if b_left and b_right:
            return True
        else:
            return False


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)

slu = Solution()
print(slu.isSymmetric(p))
