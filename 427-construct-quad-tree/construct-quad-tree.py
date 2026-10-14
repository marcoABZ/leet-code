"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        val = grid[0][0]
        final = True

        for row in grid:
            for v in row:
                if v != val:
                    final = False
                    break
            if not final:
                break 
        
        if final:
            return Node(val=val, isLeaf=True)
        return Node(
            isLeaf=False,
            topLeft=self.construct([[v for v in row[:len(row)//2]] for row in grid[:len(grid)//2]]),
            topRight=self.construct([[v for v in row[len(row)//2:]] for row in grid[:len(grid)//2]]),
            bottomLeft=self.construct([[v for v in row[:len(row)//2]] for row in grid[len(grid)//2:]]),
            bottomRight=self.construct([[v for v in row[len(row)//2:]] for row in grid[len(grid)//2:]])
        )