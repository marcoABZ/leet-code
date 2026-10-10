class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = len(nums) - 1
        swaps = 0
        while j > 0 and nums[j] == 0:
            j -= 1
        
        i = 0
        while i < j:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                swaps += 1
                while j > i and nums[j] == 0:
                    j -= 1
            else:
                i += 1
        
        return swaps
