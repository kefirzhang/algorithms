# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if not root:
            return
        if root.left is None and root.right is None:
            return root
        ptr = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(ptr)
        return root


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
slu = Solution()
t2 = slu.invertTree(t)
print(t2.right.val)
