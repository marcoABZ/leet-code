# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(val=nums[0])
    
        i, j = 0, len(nums) - 1
        rootPos = (j - i) // 2
        root = TreeNode(nums[rootPos])
        root.left = self.sortedArrayToBST(nums[:rootPos])
        root.right = self.sortedArrayToBST(nums[rootPos+1:])

        return root