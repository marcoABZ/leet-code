# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        curr = 0
        queue = [(root, 0)]
        level_sum = 0
        level_count = 0

        while queue:
            node, level = queue[0]
            queue = queue[1:]

            if level != curr:
                result.append(level_sum / float(level_count))
                curr = level
                level_sum = 0
                level_count = 0

            level_sum += node.val
            level_count += 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        result.append(level_sum / float(level_count))
        return result