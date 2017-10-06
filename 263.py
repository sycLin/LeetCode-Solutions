class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        fac = [30, 15, 10, 6, 5, 3, 2]
        for f in fac:
            while num % f == 0:
                num /= f
        return True if num == 1 else False
        
