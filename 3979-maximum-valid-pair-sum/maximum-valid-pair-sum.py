import heapq
from collections import Counter

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        c = Counter(nums[k:])
        curr = max(c.keys())
        best = 0

        for i, n in enumerate(nums[:-k]):
            if i != 0:
                c[nums[i+k-1]] -= 1

            if not c[nums[i+k-1]]:
                del c[nums[i+k-1]]
                
                if nums[i+k-1] == curr:
                    curr = max(c.keys())
            
            best = max(best, n+curr)
        
        return best