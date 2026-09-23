class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0

        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        
        for j in range(i, len(nums)):
            nums[j] = 0