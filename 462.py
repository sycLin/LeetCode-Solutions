class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in [0, 1]:
            return 0
        # find median
        nums = sorted(nums)
        if len(nums) & 1 == 0: # even length
            median = (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / 2
        else: # odd length
            median = nums[len(nums) / 2]
        
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
        