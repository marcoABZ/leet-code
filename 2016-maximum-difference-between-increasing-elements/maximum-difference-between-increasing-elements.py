class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        mn = nums[0]
        result = -1

        for n in nums:
            if n > mn:
                result = max(result, n - mn)
            else:
                mn = n
        
        return result