"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        if root.children == []:
            return 1
        depths = []
        for node in root.children:
            depths.append(self.maxDepth(node)+1)
        return max(depths)


slu = Solution()
print(slu.maxDepth())
