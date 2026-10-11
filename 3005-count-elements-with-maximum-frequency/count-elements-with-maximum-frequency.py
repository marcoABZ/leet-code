from collections import defaultdict

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1
        
        return sum([v for k, v in freqs.items() if v == max(freqs.values())])