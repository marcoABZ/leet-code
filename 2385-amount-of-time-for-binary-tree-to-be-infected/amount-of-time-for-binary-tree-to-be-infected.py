from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        adj = defaultdict(list)

        queue = [root]

        while queue:
            n = queue.pop(0)

            if n.right:
                queue.append(n.right)
                adj[n.val].append(n.right.val)
                adj[n.right.val].append(n.val)
            if n.left:
                adj[n.val].append(n.left.val)
                adj[n.left.val].append(n.val)
                queue.append(n.left)
            
        queue = [(start, 0)]
        visited = set([start])
        dist = 0

        while queue:
            curr, depth = queue.pop(0)
            for ad in adj[curr]:
                if ad not in visited:
                    queue.append((ad, depth+1))
                    dist = max(dist, depth+1)
                    visited.add(ad)
        
        return dist
