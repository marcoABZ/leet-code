from collections import defaultdict

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        def hash(word):
            return "".join(sorted(list(set(list(word)))))

        counter = defaultdict(int)

        for w in words:
            counter[hash(w)] += 1
        
        result = 0
        for v in counter.values():
            result += v * (v-1) // 2
        
        return result