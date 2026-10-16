class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        odd, even, idx = 0, 0, 0

        while n:
            if n % 2 == 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            
            idx += 1
            n >>= 1
        
        return [even, odd]