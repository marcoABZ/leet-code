# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def depth(root):
            if not root:
                return 0
        
            return 1 + max(depth(root.left), depth(root.right))
        
        if not root:
            return True
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        