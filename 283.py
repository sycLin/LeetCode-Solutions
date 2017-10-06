class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # cur1: index of the current element
        # cur2: index of the next non-zero element
        cur1, cur2 = 0, 0
        while True:
            while cur2 < len(nums) and nums[cur2] == 0:
                cur2 += 1
            if cur2 == len(nums):
                break
            nums[cur1] = nums[cur2]
            cur1, cur2 = cur1 + 1, cur2 + 1
        for i in range(cur1, len(nums)):
            nums[i] = 0
        
