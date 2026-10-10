class Solution(object):
    def largestInteger(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: int
        """
        if s == 0:
            return 0
        if s > 9 * n:
            return -1

        result = 0
        digitsLeft = n
        while digitsLeft:
            result *= 10
            digit = min(9, s)
            result += digit
            digitsLeft -= 1
            s -= digit
        
        return result
