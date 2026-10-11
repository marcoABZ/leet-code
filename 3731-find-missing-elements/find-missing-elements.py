class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        els = set([i for i in range(min(nums), max(nums)+1)])

        for n in nums:
            els.remove(n)
        
        return sorted(list(els))