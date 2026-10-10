class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        z, o, r = 0, 0, 0

        for c in s:
            if c == '0':
                z += 1
            if c == '1':
                o += 1
            
            if abs(z-o) <= 1:
                r += 1
        
        return r