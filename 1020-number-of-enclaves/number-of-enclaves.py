class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, visited, grid):
            queue = [(i, j)]
            size = 1
            conclave = True

            while queue:
                m, n = queue[0]
                queue = queue[1:]

                nxt = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]
                for n in nxt:
                    if n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0]):
                        continue 
                    if grid[n[0]][n[1]] == 0:
                        continue
                    if n in visited:
                        continue
                    if n[0] == 0 or n[0] == len(grid) - 1 or n[1] == 0 or n[1] == len(grid[0]) - 1:
                        conclave = False
                        continue
                    
                    size += 1
                    queue.append(n)
                    visited.add(n)
            
            return size if conclave else 0


        visited = set()
        result = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if (i, j) in visited:
                    continue
                
                if grid[i][j] == 0:
                    continue
                
                visited.add((i,j))
                result += dfs(i, j, visited, grid)
        
        return result