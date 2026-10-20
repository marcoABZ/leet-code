# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        def inorder(root):
            if not root:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)
        
        vals = inorder(root)
        diff = 10 ** 5 + 1

        for i in range(1, len(vals)):
            diff = min(diff, vals[i]-vals[i-1])
        
        return diff
