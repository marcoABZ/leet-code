# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(root, targetSum, path=[]):
            if not root:
                return 0
            
            result = 0
            for i in range(len(path)):
                path[i] += root.val
            path.append(root.val)

            for p in path:
                if p == targetSum:
                    result += 1

            result += dfs(root.left, targetSum, path[:])
            result += dfs(root.right, targetSum, path[:])

            return result
        
        return dfs(root, targetSum)
