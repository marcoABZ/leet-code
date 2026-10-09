# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = [root]
        values = []

        while queue:
            curr = queue[0]
            queue = queue[1:]
            if not curr:
                continue
            
            values.append(curr.val)
            queue.append(curr.right)
            queue.append(curr.left)
        
        sorted_values = sorted(values)
        result = 10**5

        for i in range(1, len(sorted_values)):
            result = min(result, sorted_values[i] - sorted_values[i-1])
        
        return result