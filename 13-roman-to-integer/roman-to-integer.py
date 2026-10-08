class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        i = 0  
        sub, tot = 0, 0  
        while i < len(s):
            if i == len(s) - 1:
                tot += values[s[i]]
                i += 1
                continue
            
            if values[s[i]] < values[s[i+1]]:
                sub += values[s[i]]
            else:
                tot += values[s[i]]
            
            i += 1

        return tot - sub 