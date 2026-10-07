class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s)

        while j > 0 and s[j-1] == '1':
            j -= 1
        
        return s[:j]