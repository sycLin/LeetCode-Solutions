# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # get length of A and B
        lenA, lenB = 0, 0
        current = headA
        while current:
            lenA += 1
            current = current.next
        current = headB
        while current:
            lenB += 1
            current = current.next
        # clip the longer one, make them start from the same level
        if lenA == 0 or lenB == 0:
            return None
        curA, curB = headA, headB
        while lenA > lenB:
            curA = curA.next
            lenA -= 1
        while lenB > lenA:
            curB = curB.next
            lenB -= 1
        # let's go!
        while curA and curB:
            if id(curA) == id(curB):
                return curA
            curA, curB = curA.next, curB.next
        return None
