# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def serialize(root):
            if not root:
                return "#"
            
            return "n" + str(root.val) + "n" + serialize(root.left) + serialize(root.right)
        
        a, b = serialize(root), serialize(subRoot)
        return b in a