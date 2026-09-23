# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        a, b = [root1], [root2]

        while a and b:
            next_leaf_a = None
            next_leaf_b = None
            while a:
                c = a[-1]
                a = a[:-1]
                if not c.left and not c.right:
                    next_leaf_a = c
                    break
                if c.right:
                    a.append(c.right)
                if c.left:
                    a.append(c.left)
            
            while b:
                c = b[-1]
                b = b[:-1]
                if not c.left and not c.right:
                    next_leaf_b = c
                    break
                if c.right:
                    b.append(c.right)
                if c.left:
                    b.append(c.left)
            
            if next_leaf_a.val != next_leaf_b.val:
                return False
        
        return not a and not b