class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        best = 0
        curr = 0

        for i, c in enumerate(s):
            if i < k and self.isVowel(c):
                curr += 1
                best += 1
            elif i >= k:
                if self.isVowel(s[i-k]):
                    curr -= 1
                if self.isVowel(c):
                    curr += 1
                best = max(best, curr)
        
        return best
    
    def isVowel(self, ch):
        return ch in ['a', 'e', 'i', 'o', 'u']