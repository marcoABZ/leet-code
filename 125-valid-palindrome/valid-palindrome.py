class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < len(s) and not s[i].isalnum():
            i += 1
        while j > i and not s[j].isalnum():
            j -= 1

        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
        
        return True