class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        if 1, 2, 3 => win, 4 => lose
        if 5, 6, 7 => win, 8 => lose
        """
        return False if n % 4 == 0 else True
