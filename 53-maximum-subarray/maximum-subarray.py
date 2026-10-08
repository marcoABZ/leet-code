class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best, curr = nums[0], nums[0]

        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(best, curr)

        return best