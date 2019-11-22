# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        n_head = head  # 指向初始原地址的指针
        pre_value = n_head.val
        n_next = n_head.next  # 指向下一个的第二个指针
        while n_next is not None:  # 遍历第二个指针到最后 更新第一个指针 最后更新第一个指针的next为None
            if n_next.val != pre_value:
                n_head.next = n_next
                n_head = n_head.next
                pre_value = n_next.val
            n_next = n_next.next
        n_head.next = None
        return head


slu = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next.next = ListNode(4)
back = slu.deleteDuplicates(head)

while back is not None:
    print(back.val)
    back = back.next
