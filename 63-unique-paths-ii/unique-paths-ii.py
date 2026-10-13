class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        result = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    result[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    continue
                elif j == 0:
                    result[i][j] = result[i-1][j]
                elif i == 0:
                    result[i][j] = result[i][j-1]
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]
            
        return result[-1][-1]