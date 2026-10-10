class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        i, j = 0, len(s) - 1
        while i < len(s) and not s[i].isalpha():
            i += 1
        
        while j > i and not s[j].isalpha():
            j -= 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

            while i < j and not s[i].isalpha():
                i += 1
            
            while j > i and not s[j].isalpha():
                j -= 1
        
        return "".join(s)