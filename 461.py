class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        mask = 1
        for i in range(32):
            if (x & mask) ^ (y & mask):
                # print(x & mask, y & mask)
                ret += 1
            x = x >> 1
            y = y >> 1
        return ret
        