class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """
        a           = 01001001
        b           = 00011101

        xor         = 01010100
        a&b         = 00001001
        a&b << 1    = 00010010

        a+b         = 01100110
        """
        mask = 0xFFFFFFFF # b/c negative number will result in infinite recursion
        if b == 0:
            return a if a <= 0x7FFFFFFF else ~(a^mask)
        print "%d, %d => %d, %d" % (a, b, (a^b) & mask, ((a&b) << 1) & mask)
        return self.getSum((a^b) & mask, ((a&b) << 1) & mask)
        
