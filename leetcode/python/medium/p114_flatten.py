# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre = root.left
            while pre.right:
                pre = pre.right
            pre.right = root.right
            root.right = root.left
            root.left = None




t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)
t1.right = TreeNode(5)
t1.left.right = TreeNode(4)
slu = Solution()
slu.flatten(t1)
