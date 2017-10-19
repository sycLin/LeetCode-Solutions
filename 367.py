class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True
        #
        # do binary search to try finding: floor(sqrt(num))
        #
        left, right = 1, num
        while left < right - 1:
            mid = (left + right) / 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared > num:
                right = mid - 1
            else:
                left = mid + 1
        if left * left != num and right * right != num:
            return False
        return True
        
