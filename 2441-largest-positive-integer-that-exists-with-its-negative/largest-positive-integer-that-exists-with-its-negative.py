class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        negs, pos = set(), set()
        result = -1

        for n in nums:
            if n > 0:
                if -n in negs:
                    result = max(result, n)
                pos.add(n)
            else:
                if -n in pos:
                    result = max(result, -n)
                negs.add(n)
        
        return result