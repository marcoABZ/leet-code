from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = 0

        for k, v in c.most_common():
            if v < 2:
                break
            result ^= k
        
        return result