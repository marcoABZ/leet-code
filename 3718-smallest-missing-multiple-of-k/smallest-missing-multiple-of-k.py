class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)
        m = 1

        while m * k in s:
            m += 1
        
        return m * k
