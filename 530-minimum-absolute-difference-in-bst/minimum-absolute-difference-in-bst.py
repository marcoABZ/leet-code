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
        order = []

        def inorder(root):
            if not root:
                return []
            
            return inorder(root.left) + [root.val] + inorder(root.right)
   
        order = inorder(root)
        result = 10**5
        for i in range(1, len(order)):
            result = min(result, order[i] - order[i-1])
        
        return result