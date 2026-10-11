class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        return s[-1] + s[-2] - s[0]