class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        r, pw = 0, 0

        while n:
            if n % 10 == 0:
                n //= 10
                continue
            r += (n % 10) * (10 ** pw)
            pw += 1
            n //= 10
        
        return r