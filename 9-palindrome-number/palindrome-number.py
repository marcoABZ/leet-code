class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        i = 0
        j = x

        while j:
            i *= 10
            i += j % 10
            j //= 10
        
        return i == x