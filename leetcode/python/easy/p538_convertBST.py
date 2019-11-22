# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.incr = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0
            self.convertBST(node.right)
            self.incr += node.val
            node.val = self.incr
            self.convertBST(node.left)
        dfs(root)
        return root


t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(13)
slu = Solution()
print(slu.convertBST(t))
