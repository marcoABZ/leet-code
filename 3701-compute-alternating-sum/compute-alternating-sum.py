class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([n if i % 2 == 0 else -n for i, n in enumerate(nums)])