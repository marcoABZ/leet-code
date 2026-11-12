from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(list(num))

        values = sorted([(k, v) for k, v in c.items()], reverse=True)
        result, last = "", ""
        
        for k, v in values:
            if v % 2 == 1 and not last:
                last = k
            
            if k == "0" and not result:
                if not last:
                    last = "0"
                continue
            result += k * (v // 2)
        
        return result + last + result[::-1]
