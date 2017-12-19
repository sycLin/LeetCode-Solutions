class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        A, B = m, n
        for a, b in ops:
            A = min(A, a)
            B = min(B, b)
        return A * B
        