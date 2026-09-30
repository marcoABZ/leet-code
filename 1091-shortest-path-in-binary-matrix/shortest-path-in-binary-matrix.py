class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        
        visited = set((0,0))
        queue = [(0,0,1)]
        while queue:
            i, j, steps = queue[0]
            queue = queue[1:]

            if i == len(grid)-1 and j == len(grid)-1:
                return steps

            dest = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            for d in dest:
                if d[0] >= 0 and d[0] < len(grid) and d[1] >= 0 and d[1] < len(grid) and grid[d[0]][d[1]] == 0 and d not in visited:
                    visited.add(d)
                    queue.append((d[0], d[1], steps+1))

        return -1