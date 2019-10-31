# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, type):
            if node is None:
                return
            if node.left is None and node.right is None and type == 1:
                self.total += node.val
            dfs(node.left, 1)
            dfs(node.right, 2)

        dfs(root.left, 1)
        dfs(root.right, 2)
        return self.total


t1 = TreeNode(2)
t1.left = TreeNode(3)
slu = Solution()
print(slu.sumOfLeftLeaves(t1))
