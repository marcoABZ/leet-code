from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set([source])
        nxt = [source]
        
        while nxt:
            curr = nxt.pop(0)

            if curr == destination:
                return True
            
            for dst in adj[curr]:
                if dst not in visited:
                    visited.add(dst)
                    nxt.append(dst)
        
        return False