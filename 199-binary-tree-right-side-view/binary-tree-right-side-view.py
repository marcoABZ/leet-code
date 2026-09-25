# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        nodes = [root]
        result = []

        while nodes:
            nxt = []
            for i, n in enumerate(nodes):
                if i == len(nodes) - 1:
                    result.append(n.val)
                
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)
            
            nodes = nxt
        
        return result