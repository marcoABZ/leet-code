class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        i, j, best = 0, k-1, nums[-1]
        while j < len(nums):
            best = min(nums[j]-nums[i], best)
            i += 1
            j += 1
        
        return best
