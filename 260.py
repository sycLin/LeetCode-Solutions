class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # xor all the numebrs
        xor_result = 0
        for num in nums:
            xor_result = xor_result ^ num

        # find a set bit and get the number
        base = 1
        while True:
            if xor_result & 1 != 0:
                break
            base = base * 2
            xor_result = xor_result >> 1
        
        # xor twice, each with/without this set bit
        xor_with = 0
        xor_without = 0
        for num in nums:
            if num & base != 0:
                xor_with = xor_with ^ num
            else:
                xor_without = xor_without ^ num
        return [xor_with, xor_without]
