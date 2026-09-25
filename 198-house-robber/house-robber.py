class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)

        nums[2]= nums[0] + nums[2]

        for i, n in enumerate(nums[3:]):
            nums[i+3] = n + max(nums[i], nums[i+1])

        return max(nums[-1], nums[-2])