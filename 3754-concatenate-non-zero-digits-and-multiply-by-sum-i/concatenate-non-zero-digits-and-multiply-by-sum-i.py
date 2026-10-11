class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, nz, p = 0, 0, 0

        while n:
            if n % 10 == 0:
                n //= 10
                continue
            
            s += n % 10
            nz += (n % 10) * (10 ** p)
            p += 1
            n //= 10
        
        return s * nz