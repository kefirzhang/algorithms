# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        savenode = listnode = ListNode('')

        while (l1 != None) or (l2 != None) or (carry != 0):
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next

            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next

            cur_val = val1 + val2 + carry
            if cur_val >= 10:
                carry = 1
                cur_val = cur_val - 10
            else:
                carry = 0

            listnode.next = ListNode(cur_val)
            listnode = listnode.next

        return savenode.next


l1 = ListNode(5)
l2 = ListNode(5)
solution = Solution()
sumnum = solution.addTwoNumbers(l1, l2)
print(sumnum.val)
print(sumnum.next.val)
