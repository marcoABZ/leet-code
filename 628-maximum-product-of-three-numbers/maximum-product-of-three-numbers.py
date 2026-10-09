import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        result = None
        if s[1] < 0:
            result = max(s[0] * s[1] * s[-1], s[-1] * s[-2] * s[-3])
        else:
            result = s[-1] * s[-2] * s[-3]
        
        return result