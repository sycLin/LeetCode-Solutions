# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # helper function
        def reverseLinkedList(head):
            cur = head
            toProcess = cur.next
            cur.next = None
            while toProcess:
                tmp = toProcess.next
                toProcess.next = cur
                cur = toProcess
                toProcess = tmp
            return cur # the new head
        def printLinkedList(head):
            cur = head
            while cur:
                print "%d ->" % (cur.val),
                cur = cur.next
            print ""

        # get length
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        check_length = length / 2

        # reverse the last $check_length$ nodes
        cur = head
        for i in range(length - check_length - 1):
            cur = cur.next
        newList = reverseLinkedList(cur.next)
        cur.next = None

        # check!!
        cur1, cur2, isPalindrome = head, newList, True
        for i in range(check_length):
            if cur1.val != cur2.val:
                isPalindrome = False
                break
            cur1 = cur1.next
            cur2 = cur2.next

        # now let's recover the list
        newList = reverseLinkedList(newList)
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = newList

        return isPalindrome

                
