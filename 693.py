class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = None
        while n > 0:
            bit = n & 1
            if last is not None and bit == last:
                return False
            else:
                last = bit
            n >>= 1
        return True