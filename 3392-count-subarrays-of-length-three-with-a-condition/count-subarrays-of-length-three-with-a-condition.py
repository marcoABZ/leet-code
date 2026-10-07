class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in range(len(nums)-2):
            if nums[i] + nums[i+2] == nums[i+1] / 2.0:
                result += 1
        
        return result