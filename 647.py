class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def countPalindromeGivenMid(left, right):
            tmpCount = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                tmpCount += 1
                left, right = left - 1, right + 1
            return tmpCount
        # count odd-length
        ret = 0
        for i in range(len(s)):
            ret += countPalindromeGivenMid(i, i)
        # count even-length
        for i in range(len(s) - 1):
            ret += countPalindromeGivenMid(i, i+1)
        return ret
        