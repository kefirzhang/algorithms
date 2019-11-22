# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_length = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def maxSameNode(node, value):
            if not node:
                return 0
            if node.val != value:
                return 0
            return maxSameNode(node.left, value) + 1 + maxSameNode(node.right, value)

        def dfs(node):
            if not node:
                return
            self.max_length = max(maxSameNode(node, node.val), self.max_length)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.max_length - 1 if self.max_length > 0 else 0


tree = TreeNode(1)
tree.right = TreeNode(1)
tree.right.right = TreeNode(1)
tree.right.left = TreeNode(1)
slu = Solution()
print(slu.longestUnivaluePath(tree))
