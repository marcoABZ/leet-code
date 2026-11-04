class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        ca, cb, result = 0, 0, 0

        for c in text:
            if c == pattern[0]:
                ca += 1
            elif c == pattern[1]:
                result += ca
                cb += 1
        
        if pattern[0] == pattern[1]:
            return (ca + 1) * ca // 2
        return result + max(ca, cb)
