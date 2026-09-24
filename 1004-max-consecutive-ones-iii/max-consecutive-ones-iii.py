class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j = 0, 0
        balance = k
        best = 0

        while j < len(nums):
            if nums[j] == 1:
                j += 1
                best = max(best, j-i)
                continue
            
            balance -= 1
            if balance >= 0:
                j += 1
                best = max(best, j-i)
                continue
            
            while i < j and nums[i] != 0:
                i += 1
            
            i += 1
            j += 1
            balance += 1
            best = max(best, j-i)
        
        return best