class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        curr = 1
        for i in range(len(nums) - 1):
            curr *= nums[-i-1]
            left.insert(0, curr)
        
        result = []
        curr = 1
        for i in range(len(nums)):
            result.append(curr * left[i])
            curr *= nums[i]
        
        return result
        

        