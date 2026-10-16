# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = [(root, 0)]
        l = 0
        levelSum = 0

        while queue:
            node, level = queue.pop(0)

            if l == level:
                levelSum += node.val
            else:
                levelSum = node.val
                l = level
            
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
        
        return levelSum