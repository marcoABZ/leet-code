from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)

        return c.most_common()[0][1] == c.most_common()[-1][1]