class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = s.split()
        if len(tokens) > 0:
            return len(tokens[-1])
        return 0
        
