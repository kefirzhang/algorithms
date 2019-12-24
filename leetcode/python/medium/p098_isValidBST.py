# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if not (node.val > lower and node.val < upper):
                return False

            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

            return

        return helper(root)


t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(1)
slu = Solution()
print(slu.isValidBST(t1))

print(float('-inf') < -1000000)
print(float('inf') > 1000000)
