# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def traverse(root, level = 0):
            if not root:
                return [(None, level)]
            
            return traverse(root.left, level+1) + [(root.val, level)] + traverse(root.right, level+1)
        
        inorder = traverse(root)
        i, j = 0, len(inorder) - 1

        while i < j:
            if inorder[i] != inorder[j]:
                return False
            i += 1
            j -= 1

        return True
        