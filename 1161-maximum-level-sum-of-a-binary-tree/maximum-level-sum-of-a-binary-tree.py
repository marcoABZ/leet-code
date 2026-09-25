# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        level = 1
        max_sum = -10**10
        max_level = 0
        nodes = [root]

        while nodes:
            level_sum = 0
            nxt = []

            for n in nodes:
                level_sum += n.val
                if n.left: nxt.append(n.left)
                if n.right: nxt.append(n.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            
            nodes = nxt
            level += 1
        
        return max_level