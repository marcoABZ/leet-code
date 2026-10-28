class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        loops = k // (n - 1)

        if loops % 2 == 0:
            return k % (n - 1)
        return n - 1 - (k % (n - 1))