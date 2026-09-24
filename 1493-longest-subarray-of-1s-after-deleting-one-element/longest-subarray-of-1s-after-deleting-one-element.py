class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        budget = 1
        best = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                best = max(best, j-i)
                continue
            
            budget -= 1
            if budget < 0:
                while i < j and not nums[i] == 0:
                    i += 1
                i += 1
            
            best = max(best, j-i)
    
        return best
