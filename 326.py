from math import log
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # method: consecutive division
        # => TLE
        """
        while n % 3 == 0:
            n /= 3
        return True if n == 1 else False
        """
        # method: using log (kinda like cheating)
        # => WA (b/c double is not precise enough)
        """
        if n <= 0:
            return False
        ret = log(n, 3)
        return True if ret == int(ret) else False
        """
        # method: better using log (kinda like still cheating)
        # => ACCEPT
        if n <= 0:
            return False
        ret = log(n, 3)
        a, b = int(ret), int(ret) + 1
        return True if n in [3**a, 3**b] else False
        
