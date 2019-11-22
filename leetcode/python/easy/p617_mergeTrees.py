# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2 is not None:
            return t2
        elif t1 is not None and t2 is None:
            return t1
        else:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node


t1 = TreeNode(1)
t2 = TreeNode(3)
slu = Solution()
print(slu.mergeTrees(t1, t2).val)
