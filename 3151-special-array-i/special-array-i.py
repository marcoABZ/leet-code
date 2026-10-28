class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        j = 1

        while j < len(nums):
            if nums[j] % 2 == nums[j-1] % 2:
                return False
            j += 1
        
        return True