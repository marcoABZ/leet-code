class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(1, len(nums)):
                nxt.append((nums[i] + nums[i-1]) % 10)
            nums = nxt

        return nums[0] 