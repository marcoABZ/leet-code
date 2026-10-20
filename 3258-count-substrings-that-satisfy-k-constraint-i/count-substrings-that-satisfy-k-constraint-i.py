from collections import Counter

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l, r, z, o = 0, 0, 0, 0
        result = 0

        while r < len(s):
            if s[r] == "0":
                z += 1
            else:
                o += 1
            
            while z > k and o > k:
                if s[l] == "0":
                    z -= 1
                else:
                    o -= 1
                l += 1
            
            result += r - l + 1
            r += 1
        
        return result