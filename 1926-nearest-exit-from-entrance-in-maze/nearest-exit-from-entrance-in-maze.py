class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        def isBorder(pos, maze):
            m, n = len(maze), len(maze[0])
            return pos[0] == 0 or pos[0] == m-1 or pos[1] == 0 or pos[1] == n-1
        
        def isEntrance(pos, entrance):
            return pos[0] == entrance[0] and pos[1] == entrance[1]
        
        def hash(pos):
            return str(pos[0]) + "/" + str(pos[1])
        
        def isValid(pos, maze):
            m, n = len(maze), len(maze[0])
            return pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n and maze[pos[0]][pos[1]] == '.'
    
        queue = [(entrance, 0)]
        visited = set([hash(entrance)])

        while queue:
            currPos, steps = queue[0]
            queue = queue[1:]

            if isBorder(currPos, maze) and not isEntrance(currPos, entrance):
                return steps
            
            movs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for mov in movs:
                i = currPos[0] + mov[0]
                j = currPos[1] + mov[1]
                if isValid([i,j], maze) and hash([i,j]) not in visited:
                    queue.append(([i,j], steps+1))
                    visited.add(hash([i,j]))
        
        return -1

