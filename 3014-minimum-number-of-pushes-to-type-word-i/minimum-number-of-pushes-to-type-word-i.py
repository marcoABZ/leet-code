from collections import defaultdict

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freqs = defaultdict(int)

        for c in word:
            freqs[c] += 1
        
        s = sorted(freqs.values(), reverse=True)
        i, r = 0, 0

        while i < len(s):
            r += sum(s[i:i+8]) * ((i // 8) + 1)
            i += 8
        
        return r
