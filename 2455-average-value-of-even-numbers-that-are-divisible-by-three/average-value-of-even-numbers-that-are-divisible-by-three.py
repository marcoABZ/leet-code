class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sm = 0
        tot = 0

        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                sm += n
                tot += 1
        
        return 0 if not tot else sm // tot