class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        return [max([len(str(grid[i][j])) for i in range(len(grid))]) for j in range(len(grid[0]))]
        