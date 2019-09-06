# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        n_head = ListNode(None)
        while head is not None:
            print(head.val)
            if n_head.next is None:
                n_head.next = ListNode(head.val)
            else:
                n_node = ListNode(head.val)
                n_node.next = n_head.next
                n_head.next = n_node
            head = head.next
        return n_head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
slu = Solution()
l2 = slu.reverseList(l1)
while l2 is not None:
    print(l2.val)
    l2 = l2.next
