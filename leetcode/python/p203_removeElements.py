# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, value: int) -> ListNode:
        pre_head = back_head = ListNode(None)
        pre_head.next = head
        while pre_head.next is not None:
            if pre_head.next.val == value:
                pre_head.next = pre_head.next.next
            else:
                pre_head = pre_head.next
        return back_head.next


l1 = ListNode(1)
l1.next = ListNode(6)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
slu = Solution()
l2 = slu.removeElements(l1, 1)
while l2 is not None:
    print(l2.val)
    l2 = l2.next
