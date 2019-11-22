# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isSameTree(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        def dfs(node):
            if not node:
                return isSameTree(node, t)
            if isSameTree(node, t):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(s)


slu = Solution()
print(slu.isSubtree())
