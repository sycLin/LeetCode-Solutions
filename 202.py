class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getSumOfSquares(n):
            ret = 0
            ret += (n%10) ** 2
            while n / 10 > 0:
                n /= 10
                ret += (n%10) ** 2
            return ret
        slow, fast = n, n
        while True:
            slow = getSumOfSquares(slow)
            fast = getSumOfSquares(getSumOfSquares(fast))
            if slow == fast:
                break

        return slow == 1
        
