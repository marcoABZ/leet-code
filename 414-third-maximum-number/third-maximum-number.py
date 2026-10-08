import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = []
        for n in nums:
            if len(top) < 3 and n not in top:
                heapq.heappush(top, n)
                continue
            
            if n > top[0] and n not in top:
                heapq.heappop(top)
                heapq.heappush(top, n)

        if len(top) < 3:
            return max(top)
        return top[0]