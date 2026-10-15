class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                left = (0, 0) if j == 0 else grid[i][j-1]
                top = (0, 0) if i == 0 else grid[i-1][j]
                diag = (0, 0) if i == 0 or j == 0 else grid[i-1][j-1]

                grid[i][j] = (
                    left[0] + top[0] - diag[0] + (1 if grid[i][j] == 
                    'X' else 0),
                    left[1] + top[1] - diag[1] + (1 if grid[i][j] == 'Y' else 0)
                )

                if grid[i][j][0] == grid[i][j][1] and grid[i][j][0] > 0:
                    result += 1
        
        return result