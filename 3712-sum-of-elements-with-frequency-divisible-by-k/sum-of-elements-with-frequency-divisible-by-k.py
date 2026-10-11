from collections import defaultdict

class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        return sum([key * v for key, v in freq.items() if v % k == 0])