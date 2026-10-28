class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(c) for c in list(s)]

        while len(s) > 2:
            new = []
        
            j = 1
            while j < len(s):
                new.append((s[j] + s[j-1]) % 10)
                j += 1
            
            s = new

        return s[0] == s[1]