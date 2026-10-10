class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        hasDigit = False

        while n:
            if n < 10 and n == x:
                return False
            
            if n % 10 == x:
                hasDigit = True
            n //= 10

        return hasDigit