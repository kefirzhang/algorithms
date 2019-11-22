# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        ret = set()

        def dfs(node, parent):
            if node is None:
                return
            if node.left is None and node.right is None:
                parent.append(str(node.val))
                ret.add("->".join(parent))
            else:
                parent.append(str(node.val))
                dfs(node.left, parent[::])
                dfs(node.right, parent[::])

        dfs(root, [])
        return list(ret)


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
slu = Solution()
print(slu.binaryTreePaths(t1))
