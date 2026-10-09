# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def best(root, prev=0):
            left, right, childPrev = 0, 0, 0
            if root.left:
                result = best(root.left, prev)
                left = 1 + result[0]
                childPrev = result[1]
            if root.right:
                result = best(root.right, prev)
                right = 1 + result[0]
                childPrev = max(childPrev, result[1])
 
            closed = 0
            if left and right:
                closed = left + right

            return max(left, right), max(prev, childPrev, closed)
        
        result = best(root)
        return max(result)

            
            