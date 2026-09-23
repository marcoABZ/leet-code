class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        curr = 1
        for i in range(len(nums) - 1):
            curr *= nums[-i-1]
            result.insert(0, curr)
        
        curr = 1
        for i in range(len(nums)):
            result[i] *= curr
            curr *= nums[i]
        
        return result
        

        