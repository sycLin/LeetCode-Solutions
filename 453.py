class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        # old => [n1, n2, n3, ..., nN]
        #
        # (... assume after X steps ...)
        #
        # new => [nx, nx, nx, ..., nx]
        #
        # therefore:
        #     1) min(old) + X = nx
        #     2) sum(old) + X * (len(old) - 1) = nx * len(old)
        # => X = nx - min(old)
        #      = (sum(old) + X * (len(old) - 1)) / len(old) - min(old)
        # => X = sum(old) - min(old) * len(old)
        #
        return sum(nums) - min(nums) * len(nums)