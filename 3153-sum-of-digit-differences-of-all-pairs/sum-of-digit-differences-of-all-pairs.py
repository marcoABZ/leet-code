from collections import Counter
from math import ceil

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        result = 0

        while nums[0]:
            c = Counter([n % 10 for n in nums])
            acc = 0

            for v in c.values():
                result += v * (len(nums) - acc - v)
                acc += v
            
            nums = [n // 10 for n in nums]
        
        return result