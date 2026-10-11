class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverse = 0
        num = n

        while num:
            reverse *= 10
            reverse += num % 10
            num //= 10
        
        return abs(n - reverse)