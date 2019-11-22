# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        head1, head2 = pre, pre

        for i in range(n):
            head2 = head2.next
            if not head2:
                return head
        while head2.next is not None:
            head1 = head1.next
            head2 = head2.next
        head1.next = head1.next.next

        return pre.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        p = ListNode(-1)
        p.next = head
        a, b = p, p

        while n > 0 and b:
            n = n - 1
            b = b.next

        if not b:
            return head

        while b.next:
            b = b.next
            a = a.next

        a.next = a.next.next

        return p.next

        '''
        for i in range(n):
            head2 = head2.next
        while head2.next is not None:
            head1 = head1.next
            head2 = head2.next
            print(head2.val, head1.val)
        print(head1.val, "*******", head1.next.next.val)
        head1.next = head1.next.next

        return pre.next
        '''


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
slu = Solution()
neddle = slu.removeNthFromEnd(head, 2)

while neddle:
    print(neddle.val)
    neddle = neddle.next
