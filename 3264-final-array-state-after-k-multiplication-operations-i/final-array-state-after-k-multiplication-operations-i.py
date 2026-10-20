import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nheap = [(v, i) for i, v in enumerate(nums)]

        heapq.heapify(nheap)
        for _ in range(k):
            v, i = heapq.heappop(nheap)
            nums[i] = v * multiplier
            heapq.heappush(nheap, (v * multiplier, i))
        
        return nums