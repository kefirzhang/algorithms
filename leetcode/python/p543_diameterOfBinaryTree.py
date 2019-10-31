# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_length = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_length = max(self.max_length, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        if self.max_length > 0:
            return self.max_length - 1
        else:
            return self.max_length


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
slu = Solution()
print(slu.diameterOfBinaryTree(t1))
