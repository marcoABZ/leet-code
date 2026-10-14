"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        traversal = []
        currLevelNodes = []
        currLevel = 1
        queue = [(root, 1)]

        while queue:
            node, level = queue[0]
            queue = queue[1:]

            if level > currLevel:
                traversal.append(currLevelNodes)
                currLevelNodes = [node.val]
                currLevel = level
            else:
                currLevelNodes.append(node.val)
            
            for c in node.children:
                queue.append((c, level+1))
        
        traversal.append(currLevelNodes)
        return traversal