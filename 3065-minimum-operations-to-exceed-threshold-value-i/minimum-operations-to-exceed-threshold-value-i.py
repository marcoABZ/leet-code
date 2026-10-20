import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = 0

        while nums[0] < k:
            heapq.heappop(nums)
            n += 1
        
        return n