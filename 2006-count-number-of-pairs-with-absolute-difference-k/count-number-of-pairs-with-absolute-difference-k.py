from collections import defaultdict

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pairs = 0
        counts = defaultdict(int)

        for n in nums:
            pairs += counts[n]
            
            counts[k+n] += 1
            counts[n-k] += 1

        return pairs