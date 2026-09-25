import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        if k == len(costs):
            return sum(costs)

        if len(costs) <= 2 * candidates:
            heapq.heapify(costs)

            total = 0
            for _ in range(k):
                total += heapq.heappop(costs)
            return total
        
        i, j = 0, len(costs) - 1
        queue = []
        for _ in range(candidates):
            heapq.heappush(queue, (costs[i], i))
            heapq.heappush(queue, (costs[j], j))
            i += 1
            j -= 1
        
        cost = 0
        for _ in range(k):
            hire_cost, index = heapq.heappop(queue)
            cost += hire_cost

            if i > j:
                continue
            elif index > j:
                heapq.heappush(queue, (costs[j], j))
                j -= 1
            else:
                heapq.heappush(queue, (costs[i], i))
                i += 1
        
        return cost
        

        
