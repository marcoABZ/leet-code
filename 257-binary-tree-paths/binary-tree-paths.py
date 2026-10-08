# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root.left and not root.right:
            return [str(root.val)]
        
        result = []
        if root.left:
            result = [str(root.val) + "->" + v for v in self.binaryTreePaths(root.left)]
        if root.right:
            result += [str(root.val) + "->" + v for v in self.binaryTreePaths(root.right)]
        
        return result