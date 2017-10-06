# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # version 1, 2, ..., n
        left  = 1 # inclusive
        right = n # inclusive
        while left < right - 1:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return left if isBadVersion(left) else right
        
