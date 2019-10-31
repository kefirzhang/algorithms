# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node'):
        ret = []

        def dfs(node):
            if node is None:
                return
            for child in node.children:
                dfs(child)
            ret.append(node.val)

        dfs(root)
        return ret


root = Node(1, [])
slu = Solution()
print(slu.postorder(root))
