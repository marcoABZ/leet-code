class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0

        for n in nums:
            if n % 3 == 0:
                continue
            ops += 1
    
        return ops