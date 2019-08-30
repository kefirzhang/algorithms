# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        if length % 2 == 0:
            root_index = int(length / 2) - 1
        else:
            root_index = int(length / 2)

        node = TreeNode(nums[root_index])
        node.left = self.sortedArrayToBST(nums[:root_index])
        node.right = self.sortedArrayToBST(nums[root_index + 1:])
        return node


slu = Solution()
print(slu.sortedArrayToBST([-10, -3, 0, 5, 9]).left.right.val)
