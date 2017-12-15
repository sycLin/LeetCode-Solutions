class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n_kinds = len(set(candies))
        n_half = len(candies) / 2
        return min(n_kinds, n_half)