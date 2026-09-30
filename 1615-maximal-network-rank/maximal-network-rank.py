class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if not roads:
            return 0

        adj = dict()

        for road in roads:
            a, b = road
            if a in adj:
                adj[a].append(b)
            else:
                adj[a] = [b]
            
            if b in adj:
                adj[b].append(a)
            else:
                adj[b] = [a]
        
        m0 = sorted(adj.items(), key=lambda x: len(x[1]), reverse=True)
        top = len(m0[0][1])
        m1 = [m for m in m0 if len(m[1]) == top]

        if len(m1) > 1:
            for i, m in enumerate(m1):
                for n in m1[i+1:]:
                    if n[0] not in adj[m[0]]:
                        return 2 * top
            return 2 * top - 1
        
        second = len(m0[1][1])
        m2 = [m for m in m0 if len(m[1]) == second]
        for m in m2:
            if m[0] not in adj[m1[0][0]]:
                return top + second
        
        return top + second - 1
        