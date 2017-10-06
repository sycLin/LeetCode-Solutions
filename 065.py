class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            ret = float(s)
        except:
            return False
        return True
        
