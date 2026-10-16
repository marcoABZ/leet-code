# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        def merge(l1, l2):
            i, j = 0, 0
            result = []

            while i < len(l1) or j < len(l2):
                a = 10**5+1 if i >= len(l1) else l1[i]
                b = 10**5+1 if j >= len(l2) else l2[j]

                if a < b:
                    result.append(a)
                    i += 1
                else:
                    result.append(b)
                    j += 1
            
            return result
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        return merge(inorder(root1), inorder(root2))