from math import ceil

class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        def generatePalindrome(first, oddDigits):
            cp = first // 10 if oddDigits else first

            while cp:
                first *= 10
                first += cp % 10
                cp //= 10
            
            return first

        middle = 10 ** ceil((intLength / 2.0) - 1)
        mx = 10 ** (ceil(intLength / 2.0))
        answer = []

        for q in queries:
            if middle + q - 1 < mx:
                answer.append(generatePalindrome(middle + q - 1, intLength % 2))
                continue
            answer.append(-1)

        return answer