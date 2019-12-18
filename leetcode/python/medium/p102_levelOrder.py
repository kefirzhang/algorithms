# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        parents = [root]
        res = []
        while parents:
            cur_values = []
            next_nodes = []
            for node in parents:
                cur_values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            parents = next_nodes
            res.append(cur_values)
        return res


l1 = TreeNode(5)
l1.left = TreeNode(1)
l1.left.left = TreeNode(4)
l1.right = TreeNode(2)
l1.right.right = TreeNode(3)
slu = Solution()
print(slu.levelOrder(l1))
