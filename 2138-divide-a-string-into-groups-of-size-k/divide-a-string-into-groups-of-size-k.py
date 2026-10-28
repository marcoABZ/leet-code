class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []

        curr = k
        while curr <= len(s):
            result.append(s[curr-k:curr])
            curr += k
        
        remainder = s[curr-k:]

        if remainder:
            while len(remainder) < k:
                remainder += fill
            result.append(remainder)
        
        return result