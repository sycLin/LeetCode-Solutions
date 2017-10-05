class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        base = 1
        for i in range(32):
            count += 1 if (base&n) > 0 else 0
            base <<= 1
        return count
        
