class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, len(s)-1

        while i <= j:
            if s[i] == s[j]:
                return i
            i += 1
            j -= 1
        
        return -1