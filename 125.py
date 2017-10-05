class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # process input string
        s = s.lower()
        s = "".join([c for c in s if 'a' <= c <= 'z' or '0' <= c <= '9'])
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
        
