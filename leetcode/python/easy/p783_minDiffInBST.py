# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.min_distance = 2 ** 32

    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        l = inorder(root)
        min_distance = 2 ** 32
        for i in range(0, len(l) - 1):
            min_distance = min(min_distance, abs(l[i + 1] - l[i]))

        return min_distance


t1 = TreeNode(96)
t1.left = TreeNode(12)
t1.left.left = TreeNode(49)
t1.left.right = TreeNode(13)
slu = Solution()
print(slu.minDiffInBST(t1))
