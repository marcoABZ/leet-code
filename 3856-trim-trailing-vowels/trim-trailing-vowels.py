class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s) - 1

        while j >= 0 and s[j] in ['a', 'e', 'i', 'o', 'u']:
            j -= 1
        
        return s[:j+1]