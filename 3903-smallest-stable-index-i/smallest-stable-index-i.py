class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r = []

        for n in nums[::-1]:
            if not r:
                r.insert(0, n)
            else:
                r.insert(0, min(r[0], n))

        top = nums[0]
        for i, n in enumerate(nums):
            top = max(top, n)
            if top - r[i] <= k:
                return i
        
        return -1
