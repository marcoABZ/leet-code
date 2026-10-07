class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counters = dict()

        for n in nums:
            if n in counters:
                counters[n] += 1
            else:
                counters[n] = 1
        
        result = 0
        for n in counters.values():
            result += (n * (n-1)) // 2

        return result