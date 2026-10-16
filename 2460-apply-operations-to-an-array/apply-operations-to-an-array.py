class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        i, j = 0, 0
        while i < len(nums) - 1:
            n = nums[i]

            if n == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            
            i+=1

        if nums[-1] != 0:
            nums[j] = nums[-1]
            j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
    
        return nums