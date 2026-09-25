# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def bfs(root, depth=1, dir=None):
            if not root:
                return depth - 1
            
            l = bfs(root.left, depth+1 if dir == 'r' else 1, 'l')
            r = bfs(root.right, depth+1 if dir == 'l' else 1, 'r')

            return max(depth, l, r)
        
        l = bfs(root.left, 1, 'l')
        r = bfs(root.right, 1, 'r')

        return max(l, r)

        