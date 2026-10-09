import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        self.vals = nums
        self.k = k
        while len(self.vals) > k:
            heapq.heappop(self.vals)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.vals) < self.k:
            heapq.heappush(self.vals, val)
            return self.vals[0]

        if val > self.vals[0]:
            heapq.heappop(self.vals)
            heapq.heappush(self.vals, val)
        return self.vals[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)