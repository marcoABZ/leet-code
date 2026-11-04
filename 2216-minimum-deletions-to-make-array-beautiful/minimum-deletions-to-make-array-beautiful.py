class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        i, j, result = 0, 1, 0

        while j < len(nums):
            if nums[j] == nums[i]:
                result += 1
            else:
                i = j+1
                j += 1
            j += 1
        
        if (len(nums) - result) % 2 == 1:
            result += 1
        return result