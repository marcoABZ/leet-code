# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue_a, queue_b = [p], [q]

        while queue_a and queue_b:
            curr_a = queue_a[0]
            curr_b = queue_b[0]

            queue_a = queue_a[1:]
            queue_b = queue_b[1:]

            if not curr_a and not curr_b:
                continue
            if not curr_a or not curr_b:
                return False
            if curr_a.val != curr_b.val:
                return False
            
            queue_a.append(curr_a.left)
            queue_a.append(curr_a.right)
            queue_b.append(curr_b.left)
            queue_b.append(curr_b.right)
        
        if queue_a or queue_b:
            return False
        return True