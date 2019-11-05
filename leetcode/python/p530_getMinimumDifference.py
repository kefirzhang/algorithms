# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        helper = []

        def dfs(node):
            if not node:
                return
            helper.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        helper.sort()
        ans = helper[-1] - helper[0]
        for i in range(len(helper) - 1):
            ans = min(ans, helper[i + 1] - helper[i])

        return ans
