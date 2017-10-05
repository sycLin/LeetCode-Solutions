class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for number in nums:
            if len(stack) == 0 or stack[-1] == number:
                stack.append(number)
            else:
                stack.pop()
        return stack[-1]
