from collections import Counter

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = 0

        for i in range(1, len(s)+1):
            c = Counter(list(s[:i]))
            if c["0"] <= k or c["1"] <= k:
                result += 1

            for j in range(i, len(s)):
                c[s[j-i]] -= 1
                c[s[j]] += 1

                if c["0"] <= k or c["1"] <= k:
                    result += 1

        return result