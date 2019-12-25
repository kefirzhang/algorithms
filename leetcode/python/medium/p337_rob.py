# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode):
        def helper(node):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return node.val, 0
            left = helper(node.left)
            right = helper(node.right)

            return node.val + left[1] + right[1], max(left[0] + right[0], left[1] + right[1], left[0] + right[1],
                                                      left[1] + right[0])

        return max(helper(root))


slu = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.right = TreeNode(3)
t1.right.right = TreeNode(1)
print(slu.rob(t1))
