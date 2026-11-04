class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        nums.sort()

        j, curr, result = 0, 0, 0
        while k > 0 and j < len(nums):
            diff = min(nums[j]-curr-1, k)
            if diff <= 0:
                curr = nums[j]
                j += 1
                continue

            k -= diff
            result += (curr+1+curr+diff) * diff // 2
            curr = nums[j]
            j += 1
        
        if k:
            result += (nums[-1]+1+nums[-1]+k) * k // 2
        return result