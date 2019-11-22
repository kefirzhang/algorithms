"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        ret = []
        childs = [root]
        cur_level = []
        cur_childs = []
        while len(childs) != 0:
            for child in childs:
                cur_level.append(child.val)
                for son in child.children:
                    cur_childs.append(son)

            ret.append(cur_level)
            childs = cur_childs
            cur_childs = []
            cur_level = []
        return ret
