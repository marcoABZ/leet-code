# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val in [0, 1]:
            return bool(root.val)
        
        if root.val == 2:
            if self.evaluateTree(root.left):
                return True
            return self.evaluateTree(root.right)
        
        if not self.evaluateTree(root.left):
            return False
        return self.evaluateTree(root.right)