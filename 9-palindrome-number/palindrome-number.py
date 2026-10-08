class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        i, j = 0, len(str(x)) - 1
        s = str(x)

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True