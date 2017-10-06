class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        trailingZeroCount = 0
        nonZeroBitCount = 0
        while num > 0:
            if num % 2 == 1:
                nonZeroBitCount += 1
            else:
                trailingZeroCount += 1
            num >>= 1
        return trailingZeroCount % 2 == 0 and nonZeroBitCount == 1
        
