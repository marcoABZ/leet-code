class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        
        result = 0
        for i, c in enumerate(s[1:]):
            if c.lower() != s[i].lower():
                result += 1
        
        return result