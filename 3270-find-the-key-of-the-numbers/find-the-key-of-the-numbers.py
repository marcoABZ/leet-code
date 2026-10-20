class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        result, i = 0, 0

        while num1 or num2 or num3:
            val = min(num1 % 10, num2 % 10, num3 % 10)
            result += val * (10 ** i)
            i += 1

            num1 //= 10
            num2 //= 10
            num3 //= 10
        
        return result