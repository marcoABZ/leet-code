class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        l, r = 0, sum(nums)
        
        for i, n in enumerate(nums):
            r -= n
            if l == r:
                return i
            l += n
        
        return -1