# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaf.append(root.val)
            else:
                dfs(root.left)
                dfs(root.right)

        leaf = []
        dfs(root1)
        leaf1 = leaf[:]
        leaf = []
        dfs(root2)
        leaf2 = leaf[:]
        # print(leaf1, leaf2)

        return leaf1 == leaf2


t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(3)
t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)
slu = Solution()
print(slu.leafSimilar(t1, t2))
