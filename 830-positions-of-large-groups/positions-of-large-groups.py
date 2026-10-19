class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        i, j = 0, 0
        result = []

        while j < len(s):
            if s[i] != s[j]:
                if j - i >= 3:
                    result.append([i, j-1])
                i = j
            j += 1
        
        if j - i >= 3:
            result.append([i, j-1])
        
        return result