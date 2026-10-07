class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)

        i = 0
        flips = 0
        while i < len(sorted_nums) and sorted_nums[i] < 0 and flips < k:
            if sorted_nums[i] < 0:
                sorted_nums[i] *= -1
                flips += 1
            
            i += 1
        
        remaining_flips = k - flips
        if remaining_flips % 2 == 0:
            return sum(sorted_nums)
        if i == 0:
            sorted_nums[0] *= -1
        elif i == len(sorted_nums):
            sorted_nums[-1] *= -1
        else:
            if sorted_nums[i] < sorted_nums[i-1]:
                sorted_nums[i] *= -1
            else:
                sorted_nums[i-1] *= -1
        
        return sum(sorted_nums)
