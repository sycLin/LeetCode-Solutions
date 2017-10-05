class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 1
        ret = 0
        for c in s[::-1]:
            ret += ((ord(c) - ord('A')) + 1) * base
            base *= 26
        return ret
        
