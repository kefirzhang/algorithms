# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = rserialize(node.left, string)
                string = rserialize(node.right, string)
            return string

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        return rdeserialize(data_list)


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
slu = Codec()
strt1 = slu.serialize(t1)
print(strt1)
t2 = slu.deserialize(strt1)
print(t2.left.val)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
