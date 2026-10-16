class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        averages = set()

        i, j = 0, len(nums) - 1
        while i < j:
            averages.add((nums[j] + nums[i]) / 2.0)
            i += 1
            j -= 1
        
        return len(averages)