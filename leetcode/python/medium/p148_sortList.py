# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList2(self, head: ListNode) -> ListNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.sort()
        node = new_head = ListNode(None)
        for i in values:
            new_head.next = ListNode(i)
            new_head = new_head.next

        return node.next
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)

        res = pre = ListNode(0)
        while left and right:
            if left.val < right.val:
                pre.next, left = left, left.next
            else:
                pre.next, right = right, right.next
            pre = pre.next
        if left or right:
            pre.next = left if left else right

        return res.next


l1 = ListNode(5)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(3)
slu = Solution()
l1 = slu.sortList(l1)
while l1:
    print(l1.val)
    l1 = l1.next
