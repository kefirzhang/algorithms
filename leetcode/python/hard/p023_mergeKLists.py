# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        head = pre = ListNode(None)
        nodeVals = []
        for l in lists:
            while l:
                nodeVals.append(l.val)
                l = l.next

        for i in sorted(nodeVals):
            pre.next = ListNode(i)
            pre = pre.next
        return head.next
