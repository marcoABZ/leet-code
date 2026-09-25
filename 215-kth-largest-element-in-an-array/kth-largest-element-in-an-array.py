import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []

        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
                continue

            if n > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, n)
        
        return heapq.heappop(h)
        