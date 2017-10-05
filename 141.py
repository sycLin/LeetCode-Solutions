# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        oneStepper = head
        twoStepper = head
        while oneStepper != None and twoStepper != None:
            oneStepper = oneStepper.next
            twoStepper = twoStepper.next.next if twoStepper.next else None
            if oneStepper and twoStepper and id(oneStepper) == id(twoStepper):
                return True
        return False
        
