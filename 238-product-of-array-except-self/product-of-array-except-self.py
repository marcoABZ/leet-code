class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = [1]
        curr = 1
        for n in nums[:len(nums)-1]:
            curr *= n
            right.append(curr)

        left = [1]
        curr = 1
        for i in range(len(nums) - 1):
            curr *= nums[-i-1]
            left.insert(0, curr)
        
        result = []
        for i in range(len(nums)):
            result.append(right[i] * left[i])
        
        return result
        

        