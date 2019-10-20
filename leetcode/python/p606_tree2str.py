# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        ret = str(t.val)
        if t.left is None and t.right is None:
            return ret
        elif t.right is None:
            return ret + "(" + self.tree2str(t.left) + ")"
        else:
            return ret + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.right = TreeNode(3)

slu = Solution()
print(slu.tree2str(tree))
