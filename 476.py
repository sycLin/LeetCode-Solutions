class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bits = bin(num)[2:] # skip "0b" at the beginning
        bits = bits.lstrip("0") # remove leading 0's
        bits = "".join("0" if b == "1" else "1" for b in bits)
        return int(bits, 2)
        