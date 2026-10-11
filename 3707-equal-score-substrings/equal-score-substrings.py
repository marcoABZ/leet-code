class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r = sum([ord(c) - ord('a') + 1 for c in s])
        l = 0

        for c in s:
            sc = ord(c) - ord('a') + 1
            r -= sc
            l += sc

            if l == r:
                return True
            elif l > r:
                return False
        
        return False