import heapq

class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = sum(nums)

        h = [-n for n in nums]
        heapq.heapify(h)

        ops = 0
        curr = tot
        while curr > tot / 2.0:
            el = -heapq.heappop(h)
            curr -= el / 2.0
            heapq.heappush(h, -el / 2.0)
            ops += 1
        
        return ops