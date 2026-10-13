class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]

        k, i, v = 0, 0, 1
        while k <= n // 2:
            for j in range(k, n-k):
                result[k][j] = v
                v += 1
            for j in range(k+1, n-k):
                result[j][n-k-1] = v
                v += 1
            for j in range(n-k-1, k, -1):
                result[n-k-1][j-1] = v
                v += 1
            for j in range(n-k-1, k+1, -1):
                result[j-1][k] = v
                v += 1
            k += 1
        
        return result
