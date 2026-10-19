class Solution:
    def binaryGap(self, n: int) -> int:
        lastOne = None
        largestGap = 0
        i = 1

        while n:
            if n % 2 == 1:
                if lastOne:
                    largestGap = max(largestGap, i-lastOne)
                lastOne = i
            i += 1
            n >>= 1
        
        return largestGap