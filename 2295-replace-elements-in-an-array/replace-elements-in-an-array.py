class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        idx = {n: i for i, n in enumerate(nums)}

        for original, new in operations:
            i = idx[original]
            del idx[original]
            idx[new] = i
        
        for k, v in idx.items():
            nums[v] = k
        
        return nums