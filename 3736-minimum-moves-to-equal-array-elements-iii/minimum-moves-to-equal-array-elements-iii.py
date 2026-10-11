class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(nums)
        return sum([mx - n for n in nums])