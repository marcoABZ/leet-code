class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n-1)) and (n - 1) % 3 == 0