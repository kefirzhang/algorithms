# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False

        b_left = self.isSameTree(p.left, q.left)
        b_right = self.isSameTree(p.right, q.right)

        if b_left and b_right:
            return True
        else:
            return False


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)

slu = Solution()
print(slu.isSameTree(p, q))
