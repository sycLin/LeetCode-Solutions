class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_init = 0
        for num in nums:
            xor_init ^= num
        return xor_init
        
