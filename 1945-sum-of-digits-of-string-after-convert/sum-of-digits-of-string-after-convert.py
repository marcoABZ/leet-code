class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ""

        for c in s:
            convert += str(ord(c) - ord('a') + 1)
        
        val = int(convert)
        for _ in range(k):
            nxt = 0
            while val:
                nxt += val % 10
                val //= 10
            val = nxt

        return val