# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_num
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            new_path = node.val + left_gain + right_gain
            max_num = max(max_num, new_path)
            return node.val + max(left_gain, right_gain)

        max_num = float('-inf')
        max_gain(root)
        return max_num


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
slu = Solution()
print(slu.maxPathSum(t1))
