from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        sz = len(s)

        while sz > 2:
            for i in range(len(s)-sz+1):
                c = Counter(s[i:i+sz])
                if c.most_common()[0][1] <= 2:
                    return sz
            sz -= 1
        
        return 2

