# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        helper = set()
        def inorder(node):
            if not node:
                return
            helper.add(node.val)
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        helper = list(helper)
        helper.sort()
        if len(helper) < 2:
            return -1
        return helper[1]

