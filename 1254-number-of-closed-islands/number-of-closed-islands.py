class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, visited, grid):
            closed = True

            queue = [(i, j)]
            while queue:
                p, q = queue[0]
                queue = queue[1:]

                neighbors = [(p+1, q), (p-1, q), (p, q+1), (p, q-1)]

                for n in neighbors:
                    if (n[0] == 0 or n[0] == len(grid)-1 or n[1] == 0 or n[1] == len(grid[0])-1) and grid[n[0]][n[1]] == 0:
                        closed = False
                        continue
                    
                    if grid[n[0]][n[1]] == 1:
                        continue
    
                    if n in visited:
                        continue
                    
                    visited.add(n)
                    queue.append(n)

            return closed
        
        result = 0
        visited = set()
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1 or (i, j) in visited:
                    continue
                
                visited.add((i, j))
                if dfs(i, j, visited, grid):
                    result += 1
        
        return result