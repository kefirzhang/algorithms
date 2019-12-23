# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersect(self, head: ListNode):
        hare = head
        tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return hare

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        ptr2 = self.getIntersect(head)
        if ptr2 is None:
            return None
        ptr1 = head

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
