# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        seen = set()
        notRoot = set()
        nodes = dict()

        for parent, child, left in descriptions:
            nd = None
            if child in nodes:
                nd = nodes[child]
            else:
                nd = TreeNode(val=child)
                nodes[child] = nd

            p = None
            if parent in nodes:
                p = nodes[parent]
            else:
                p = TreeNode(val=parent)
                nodes[parent] = p
            
            if left:
                p.left = nd
            else:
                p.right = nd

            seen.add(child)
            seen.add(parent)
            notRoot.add(child)

        return nodes[list((seen-notRoot))[0]]