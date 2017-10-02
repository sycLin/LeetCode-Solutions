# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current:
            while current.next:
                if current.next.val == current.val:
                    current.next = current.next.next
                else:
                    break
            current = current.next
        return head
        
