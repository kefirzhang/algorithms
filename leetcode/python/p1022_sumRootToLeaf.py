# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:

        def dfs(node, parent):
            if node is None:
                return
            if node.left is None and node.right is None:
                parent.append(str(node.val))
                print(parent)
                self.ans += int("".join(parent), base=2)
            else:
                parent.append(str(node.val))
                dfs(node.left, parent[::])
                dfs(node.right, parent[::])

        dfs(root, [])
        return self.ans


t1 = TreeNode(1)
t1.left = TreeNode(0)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(0)
t1.right = TreeNode(1)
t1.right.left = TreeNode(0)
t1.right.right = TreeNode(1)
slu = Solution()
print(slu.sumRootToLeaf(t1))
