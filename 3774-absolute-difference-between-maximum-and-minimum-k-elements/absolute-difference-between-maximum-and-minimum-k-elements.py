class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = sorted(nums)

        return abs(sum(n[:k]) - sum(n[-k:]))   