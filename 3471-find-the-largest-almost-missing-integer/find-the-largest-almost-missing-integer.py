class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)

        if k == len(nums):
            candidates = nums
        elif k == 1:
            candidates = [k for k,v in c.items() if v == 1]
        else:
            candidates = [n for n in [nums[0], nums[-1]] if c[n] == 1]
        
        if not candidates:
            return -1
        return max(candidates)