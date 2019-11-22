# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        niddle_a = head
        niddle_b = head.next

        while niddle_a != niddle_b:
            niddle_a = niddle_a.next
            if niddle_b.next is None:
                return False
            niddle_b = niddle_b.next.next
            if niddle_b is None:
                return False
        return True

        """
        :type head: ListNode
        :rtype: bool
        """

l1 = ListNode(1)
#l1.next = ListNode(2)
#l1.next.next = l1
slu = Solution()
print(slu.hasCycle(l1))

