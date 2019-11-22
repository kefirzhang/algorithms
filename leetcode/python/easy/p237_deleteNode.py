# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
l1 = ListNode(1)
l1.next = ListNode(6)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
slu = Solution()
l2 = slu.deleteNode(l1.next.next.next)
while l2 is not None:
    print(l2.val)
    l2 = l2.next
