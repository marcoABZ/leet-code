class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = []

        for i in range(len(grid)):
            row = grid[i] if i % 2 == 0 else grid[i][::-1]
            j = 0 if i % 2 == 0 or len(row) % 2 == 0 else 1
            while j < len(row):
                result.append(row[j])
                j += 2
        
        return result

