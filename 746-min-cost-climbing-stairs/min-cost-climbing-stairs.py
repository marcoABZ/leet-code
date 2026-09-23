class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costs = cost[:]

        for i in range(2, len(cost)):
            costs[i] = min(costs[i-2], costs[i-1]) + costs[i]
        
        return min(costs[-1], costs[-2])