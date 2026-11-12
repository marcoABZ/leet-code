from math import floor

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def getDivisors(n):
            count, sm = 0, 0

            for i in range(1, floor(n**0.5) + 1):
                if n % i == 0:
                    sm += i
                    count += 1

                    if i != n // i:
                        sm += n // i
                        count += 1

            return count, sm

        return sum([getDivisors(n)[1] for n in nums if getDivisors(n)[0] == 4])