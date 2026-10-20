class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for j in range(len(matrix[0])):
            val = matrix[0][j]
            for i in range(len(matrix)):
                if j+i < len(matrix[0]) and matrix[i][j+i] != val:
                    return False
        
        for i in range(len(matrix)):
            val = matrix[i][0]
            for j in range(len(matrix[0])):
                if i+j < len(matrix) and matrix[i+j][j] != val:
                    return False
        
        return True


