# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        b = s = ListNode('')

        while l1 is not None and l2 is not None:
            #print(l1.val, l2.val)
            if l1.val <= l2.val:
                s.next = ListNode(l1.val)
                l1 = l1.next
            else:
                s.next = ListNode(l2.val)
                l2 = l2.next
            s = s.next

        if l1 != None:
            s.next = l1
        if l2 != None:
            s.next = l2

        return b.next


slu = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s = slu.mergeTwoLists(l1, l2)
while s != None:
    print(s.val)
    s = s.next
