import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)

        words = Counter([w.lower() for w in re.split(r"[ !?',;.]", paragraph) if w and w.lower() not in banned])

        return words.most_common(1)[0][0]