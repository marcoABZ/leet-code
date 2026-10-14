class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 and k % 2 == 1:
            return -1
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]

        if k > len(nums):
            return max(nums)
        elif k == len(nums):
            return max(nums[:k-1])
        return max(max(nums[:k-1]), nums[k])