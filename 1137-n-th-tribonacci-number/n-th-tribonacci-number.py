class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        i, j, k = 0, 1, 1
        for _ in range(n-2):
            i, j, k = j, k, i + j + k
        
        return k