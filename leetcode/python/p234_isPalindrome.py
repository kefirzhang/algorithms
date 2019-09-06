# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        n_head = ListNode(None)
        while head is not None:
            if n_head.next is None:
                n_head.next = ListNode(head.val)
            else:
                n_node = ListNode(head.val)
                n_node.next = n_head.next
                n_head.next = n_node
            head = head.next
        return n_head.next

    def isPalindrome(self, head: ListNode) -> bool:
        r_head = self.reverseList(head)
        while r_head is not None and head is not None and r_head.val == head.val:
            r_head = r_head.next
            head = head.next
        if r_head is not None or head is not None:
            return False
        return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(1)
slu = Solution()
print(slu.isPalindrome(l1))
