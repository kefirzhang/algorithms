# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node, val):
            if node is None:
                return True
            if node.val != val:
                return False
            return dfs(node.left, val) and dfs(node.right, val)

        if root is None:
            return True
        return dfs(root, root.val)
