class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 0 if all([n == nums[0] for n in nums]) else 1