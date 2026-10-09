# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        second = None

        queue = [root]
        while queue:
            curr = queue[0]
            queue = queue[1:]

            if curr.val != root.val:
                if second is None:
                    second = curr.val
                else:
                    second = min(second, curr.val)
                continue

            if curr.right:
                queue.append(curr.right)
                queue.append(curr.left)

        return second if second is not None else -1