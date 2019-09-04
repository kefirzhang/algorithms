# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, heada, headb):
        n_heada = heada  # 标记 头指针
        n_headb = headb  # 标记 头指针
        if heada is None or headb is None:
            return
        while n_heada is not None or n_headb is not None:
            if n_heada is None:
                n_heada = headb
            if n_headb is None:
                n_headb = heada

            if n_heada == n_headb:
                return n_heada

            n_heada = n_heada.next
            n_headb = n_headb.next

        return




l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(0)
l2.next.next = ListNode(1)
l2.next.next.next = l1.next.next

slu = Solution()
print(slu.getIntersectionNode(l1, l2))
