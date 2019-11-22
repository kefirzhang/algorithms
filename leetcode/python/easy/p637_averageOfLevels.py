# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode):
        ret = []
        level = [root]
        storage_level = []
        storage_val = []
        while len(level) > 0:
            for node in level:
                storage_val.append(node.val)
                if node.left:
                    storage_level.append(node.left)
                if node.right:
                    storage_level.append(node.right)
            # print(sum(storage_val), len(storage_val))
            ret.append(sum(storage_val) / len(storage_val))
            level = storage_level
            storage_level = []
            storage_val = []

        return ret


'''
[3,9,20,15,7]
'''
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.left.left = TreeNode(15)
t1.left.right = TreeNode(7)
slu = Solution()
print(slu.averageOfLevels(t1))
