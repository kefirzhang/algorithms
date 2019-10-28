# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 问题 在广度和深度中想着返回 这样不好理解 还不如 全部遍历 然后全局变量保存 这样好很多
class Solution:
    def getNodeINfo(self, root, node, depth=1):

        if root is None:
            return False
        if (root.left is not None and root.left.val == node) or (root.right is not None and root.right.val == node):
            return [root.val, depth]
        else:
            left = self.getNodeINfo(root.left, node, depth + 1)
            right = self.getNodeINfo(root.right, node, depth + 1)
            if left is not False:
                return left
            elif right is not False:
                return right
            else:
                return False
        return False  # 父节点 深度

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        y_info = self.getNodeINfo(root, y, 1)
        x_info = self.getNodeINfo(root, x, 1)
        if x_info is False or y_info is False:
            return False
        if x_info[0] == y_info[0] or x_info[1] != y_info[1]:  # 深度相同 父节点不同
            return False
        return True


tree = TreeNode(1)

tree.left = TreeNode(2)
tree.left.left = TreeNode(5)

tree.right = TreeNode(3)
tree.right.right = TreeNode(4)

slu = Solution()
print(slu.isCousins(tree, 5, 4))
