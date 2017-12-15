class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # form the look-up dict
        # which maps numbers to their "next greater element"
        #
        # Method #1: time complexity = O(n^2), about 70 ms
        # Result: Accepted
        #
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = -1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    d[nums[i]] = nums[j]
                    break
        return [d[num] for num in findNums]
            
        