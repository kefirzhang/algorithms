# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(node, target):

            if node is None:
                return
            print(node.val, target)
            if node.val == target:
                self.ans += 1
                dfs(node.left, sum)
                dfs(node.right, sum)

            else:
                dfs(node.left, target - node.val)
                dfs(node.right, target - node.val)
                dfs(node.left, sum)
                dfs(node.right, sum)

        dfs(root, sum)
        return self.ans


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.right.right = TreeNode(4)
tree.right.right.right.right = TreeNode(5)

slu = Solution()
print(slu.pathSum(tree, 3))
