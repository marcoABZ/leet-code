# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def tilt(root):
            if not root:
                return 0, 0
            
            left, right = tilt(root.left), tilt(root.right)
            return left[0] + right[0] + abs(right[1] - left[1]), root.val + right[1] + left[1]
        
        return tilt(root)[0]
