# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        count = dict()
        queue = [root]

        while queue:
            curr = queue[0]
            queue = queue[1:]

            if curr.val in count:
                count[curr.val] += 1
            else:
                count[curr.val] = 1
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        values = sorted([(v, k) for k, v in count.items()], key=lambda x: x[0], reverse=True)

        return [v[1] for v in values if v[0] == values[0][0]]

        