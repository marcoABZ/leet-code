from collections import defaultdict

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = defaultdict(int)
        best = 0

        for n in nums:
            counts[n] += 1
            plus = counts[n] + counts[n+1] if counts[n+1] else 0
            minus = counts[n] + counts[n-1] if counts[n-1] else 0

            best = max(best, plus, minus)
        
        return best
