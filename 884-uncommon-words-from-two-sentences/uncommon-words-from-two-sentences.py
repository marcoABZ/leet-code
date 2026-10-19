from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        candidates = Counter(s1.split(" "))
        filtered = Counter({k: v for k, v in candidates.items() if v == 1})

        candidates2 = Counter(s2.split(" "))
        filtered2 = Counter({k: v for k, v in candidates2.items() if v == 1})
        
        #print(filtered, filtered2, filtered - filtered2, filtered2 - filtered)
        return list((filtered - candidates2).keys()) + list((filtered2 - candidates).keys())
