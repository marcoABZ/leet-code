class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r, c = False, False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

                    if i == 0:
                        r = True
                    if j == 0:
                        c = True

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0 if matrix[i][0] == 0 or matrix[0][j] == 0 else matrix[i][j]
        
        if r:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if c:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        return matrix