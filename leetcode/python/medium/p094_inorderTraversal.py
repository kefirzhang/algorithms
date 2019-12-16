# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        def helper(node: TreeNode):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res


slu = Solution()

t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(3)
print(slu.inorderTraversal(t1))

'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return 
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res
'''