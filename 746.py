class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #
        # Let's use DP and with bottom-up building
        # since recursion will cause stack overflow.
        #
        return self._buildMinCost(cost)[-1]
    
    def _buildMinCost(self, cost):
        # init
        minCost = [0 for _ in range(len(cost) + 1)]
        # build
        for i in range(2, len(cost) + 1):
            minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])
        return minCost
        