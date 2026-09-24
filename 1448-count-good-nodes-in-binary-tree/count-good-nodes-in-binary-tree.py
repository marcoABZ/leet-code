# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, largest=-10**5):
            if not root:
                return 0

            result = 0
            if root.val >= largest:
                result += 1
                largest = root.val
            
            result += dfs(root.left, largest)
            result += dfs(root.right, largest)

            return result

        return dfs(root)
