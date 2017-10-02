class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0 or x == 1:
            return x
        # do binary search to find the sqrt(x)
        start, end = 1, x # both inclusive
        while start < end-1:
            mid = (start + end) / 2
            if mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid
            else:
                return mid
        return start

    """
    0 1 2 3 4 5
    """
