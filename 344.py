class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # method: using list.reverse()
        # => ACCEPT
        l = [c for c in s]
        l.reverse()
        return "".join(l)
        # method: using string index subscription
        # => ACCEPT (faster than above)
        return s[::-1]
        
