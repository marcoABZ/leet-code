# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        def univalHelper(root):
            if not root:
                return (0, 0)
            
            left = univalHelper(root.left)
            right = univalHelper(root.right)
            
            continuingL, continuingR = 1, 1
            withSelf = 1
            if root.left and root.left.val == root.val:
                continuingL += left[0]
                withSelf += left[0]
            if root.right and root.right.val == root.val:
                continuingR += right[0]
                withSelf += right[0]

            return (max(continuingR, continuingL), max(left[0], left[1], right[0], right[1], withSelf))
        
        if not root:
            return 0
        return max(univalHelper(root)) - 1