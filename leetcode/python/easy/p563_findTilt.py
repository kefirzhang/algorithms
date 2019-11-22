# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            self.ans += tilt(node)
            dfs(node.left)
            dfs(node.right)

        def dfs_total(node):
            if not node:
                return 0
            return dfs_total(node.left) + node.val + dfs_total(node.right)

        def tilt(node):
            if node is None:
                return 0
            return abs(dfs_total(node.left) - dfs_total(node.right))
        dfs(root)
        return self.ans


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
slu = Solution()
print(slu.findTilt(tree))