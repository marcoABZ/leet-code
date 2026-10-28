class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        mn = nums[-1]
        i, j = 0, len(nums) - 1
        
        while i < j:
            mn = min(mn, (nums[i] + nums[j]) / 2.0)
            i += 1
            j -= 1
        
        return mn