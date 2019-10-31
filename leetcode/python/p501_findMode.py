# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode):
        helper = {}

        def dfs(node):
            if node is None:
                return None
            dfs(node.left)
            dfs(node.right)
            if helper.__contains__(node.val):
                helper[node.val] += 1
            else:
                helper[node.val] = 1

        dfs(root)
        ret = []
        ret_times = 0
        for i in helper:
            if helper[i] > ret_times:
                ret = []
                ret.append(i)
                ret_times = helper[i]
            elif helper[i] == ret_times:
                ret.append(i)
        return ret


t1 = TreeNode(1)
t1.left = TreeNode(1)
t1.right = TreeNode(2)
t1.left.left = TreeNode(2)
slu = Solution()
print(slu.findMode(t1))
