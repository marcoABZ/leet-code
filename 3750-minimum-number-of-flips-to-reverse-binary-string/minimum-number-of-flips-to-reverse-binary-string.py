class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn, rbn = "", ""

        while n:
            bn = str(n % 2) + bn
            rbn += str(n % 2)
            n //= 2
        
        flips = 0
        for i in range(len(bn)):
            if bn[i] != rbn[i]:
                flips += 1
        
        return flips