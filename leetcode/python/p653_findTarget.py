# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        helper = []
        def dfs(node):
            if not node:
                return
            helper.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        helper.sort()
        i, j = 0, len(helper) - 1
        while i < j:
            sum_num = helper[i] + helper[j]
            if sum_num == k:
                return True
            elif sum_num > k:
                j -= 1
            else:
                i += 1
        return False


t1 = TreeNode(2)
t1.left = TreeNode(0)
t1.right = TreeNode(3)
t1.left.left = TreeNode(-4)
t1.left.right = TreeNode(1)
slu = Solution()
print(slu.findTarget(t1, -1))
