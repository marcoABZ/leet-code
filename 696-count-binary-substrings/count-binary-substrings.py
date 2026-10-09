class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastRep = 0
        repeated = 0
        curr = None
        result = 0

        for c in s:
            if c == curr:
                repeated += 1
            else:
                result += min(lastRep, repeated)
                lastRep = repeated
                curr = c
                repeated = 1
        
        result += min(lastRep, repeated)
        return result