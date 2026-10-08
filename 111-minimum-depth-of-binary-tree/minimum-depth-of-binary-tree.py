# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        left, right = 10**5 + 1, 10**5 + 1
        if root.left:
            left = 1 + self.minDepth(root.left)
        if root.right:
            right = 1 + self.minDepth(root.right)
        return min(left, right)