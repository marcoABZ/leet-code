from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        ranks = defaultdict(int)
        parents = defaultdict(int)

        def find(nd):
            if not parents[nd]:
                return nd
            return find(parents[nd])
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            if ranks[pa] > ranks[pb]:
                parents[pb] = pa
            elif ranks[pb] > ranks[pa]:
                parents[pa] = pb
            else:
                parents[pb] = pa
                ranks[pa] += 1
            return True
        
        last = None
        for x, y in edges:
            if not union(x, y):
                last = [x,y]
        
        return last