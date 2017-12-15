class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        current_counter = 0
        for num in nums:
            if num == 0:
                longest = max(longest, current_counter)
                current_counter = 0
            else:
                current_counter += 1
        return max(longest, current_counter)