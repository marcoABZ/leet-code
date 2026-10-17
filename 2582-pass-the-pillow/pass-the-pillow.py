class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        balance = time % ((n-1) * 2)

        if balance < n:
            return balance + 1
        return n - (balance - n) - 1