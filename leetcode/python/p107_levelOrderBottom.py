# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        d_nodes_val = []  # 返回的数据数组
        c_nodes_val = []  # 存储当前一层的val
        n_nodes = []  # 临时存储下一层的节点
        nodes = [root]  # 从根结点开始遍历
        while len(nodes) > 0:
            node = nodes.pop(0)

            c_nodes_val.append(node.val)

            if node.left is not None:
                n_nodes.append(node.left)
            if node.right is not None:
                n_nodes.append(node.right)

            if len(nodes) == 0 and len(n_nodes) != 0:
                nodes = n_nodes
                n_nodes = []
                d_nodes_val.append(c_nodes_val)
                c_nodes_val = []
        d_nodes_val.append(c_nodes_val)
        d_nodes_val.reverse()
        return d_nodes_val


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(4)
slu = Solution()
print(slu.levelOrderBottom(p))
