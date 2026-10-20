from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        letters = Counter([c.lower() for c in list(licensePlate) if c.isalpha()])

        result = None
        for word in words:
            if result is not None and len(word) >= len(result):
                continue

            if Counter(list(word)) >= letters:
                result = word
        
        return result