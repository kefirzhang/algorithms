# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right

        return ans.right


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
slu = Solution()
t2 = slu.increasingBST(tree)
while t2:
    print(t2.val)
    t2 = t2.right
