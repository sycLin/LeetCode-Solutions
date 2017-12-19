from math import sqrt

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        searchStart = int(sqrt(area))
        for i in range(searchStart, 0, -1):
            if area % i == 0:
                return [area / i, i]
        