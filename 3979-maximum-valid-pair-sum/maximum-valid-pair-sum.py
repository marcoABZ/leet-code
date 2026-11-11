from collections import Counter

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        topVals = []
        for n in nums[k:][::-1]:
            if not topVals:
                topVals.append(n)
            else:
                topVals.insert(0, max(n, topVals[0]))

        best = 0

        for i, n in enumerate(nums[:-k]):
            best = max(best, n+topVals[i])
        
        return best