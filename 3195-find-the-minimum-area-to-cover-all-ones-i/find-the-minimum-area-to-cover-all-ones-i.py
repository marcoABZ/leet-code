class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minI, minJ, maxI, maxJ = len(grid), len(grid[0]), 0, 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    minI = min(minI, i)
                    maxI = i
                    minJ = min(minJ, j)
                    maxJ = max(maxJ, j)
        
        return (maxI-minI+1) * (maxJ-minJ+1)
