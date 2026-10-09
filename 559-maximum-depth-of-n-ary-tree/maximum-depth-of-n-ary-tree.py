"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        queue = [(root, 1)]
        result = 0

        while queue:
            curr, depth = queue[0]
            queue = queue[1:]
            result = max(result, depth)

            for c in curr.children:
                queue.append((c, depth+1))
        
        return result