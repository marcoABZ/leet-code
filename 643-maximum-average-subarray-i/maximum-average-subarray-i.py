class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = 0
        best = -10**5
        for i, n in enumerate(nums):
            if i < k - 1:
                curr += n
                continue
            
            curr += n
            best = max(best, float(curr) / k)
            curr -= nums[i-k+1]
        
        return best