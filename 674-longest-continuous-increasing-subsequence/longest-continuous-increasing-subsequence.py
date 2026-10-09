class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, best = 0, 1, 1

        while j < len(nums):
            if nums[j-1] >= nums[j]:
                best = max(best, j-i)
                i = j
            j += 1
        
        return max(best, j-i)