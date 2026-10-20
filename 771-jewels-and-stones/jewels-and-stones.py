class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(list(jewels))
        result = 0

        for s in stones:
            if s in jewels:
                result += 1
        
        return result