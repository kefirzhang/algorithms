# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = (node == p or node == q)
            if mid + left + right >= 2:
                self.res = node

            return mid or left or right

        dfs(root)
        return self.res


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(7)

slu = Solution()
t2 = slu.lowestCommonAncestor(t1, t1, t1.left.right)
print(t2.val)
