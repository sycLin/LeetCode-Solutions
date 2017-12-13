class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Time: O(N^2)
        # Result: TLE
        """
        n = len(height)
        M = float('-INF')
        for left in range(n):
            for right in range(left+1, n):
                contain = min(height[left], height[right]) * (right - left)
                M = max(contain, M)
        return M
        """
        # Time: O(N)
        # Result: ACCEPT
        left, right = 0, len(height) - 1
        M = float('-INF')
        while left < right:
            contain = min(height[left], height[right]) * (right - left)
            M = max(M, contain)
            # move left / right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return M
        
        