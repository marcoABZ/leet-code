class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ss, ds = 0, 0

        while n:
            ss += (n % 10) ** 2
            ds += n % 10
            n //= 10
        
        return ss - ds >= 50