class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        idx = dict()

        for i, c in enumerate(s):
            idx[c] = i
        
        result = 0
        for i, c in enumerate(t):
            result += abs(i - idx[c])
        
        return result