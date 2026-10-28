class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        columnsValid = all([len(set([grid[i][j] for i in range(len(grid))])) == 1 for j in range(len(grid[0]))])
        if not columnsValid:
            return False

        val = grid[0][0]
        for v in grid[0][1:]:
            if v == val:
                return False
            val = v

        return True