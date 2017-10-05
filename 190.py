class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        base = 1
        ret = 0
        for i in range(32):
            bit = n & base
            base *= 2
            ret = ret * 2 + 1 if bit > 0 else ret * 2
        return ret
        
