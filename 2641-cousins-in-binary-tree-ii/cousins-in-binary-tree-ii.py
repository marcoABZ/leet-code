# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        level = [root]
        levelSum = root.val

        while level:
            nxLevel = []
            nxLevelSum = 0

            for n in level:
                n.val = levelSum - n.val
                if n.left:
                    nxLevelSum += n.left.val
                    nxLevel.append(n.left)
                    if n.right:
                        n.left.val += n.right.val

                if n.right:
                    nxLevelSum += n.right.val
                    nxLevel.append(n.right)
                    if n.left:
                        n.right.val += n.left.val - n.right.val

            level = nxLevel
            levelSum = nxLevelSum

        return root 