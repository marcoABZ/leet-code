class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ranks = [0 for _ in range(n)]

        for edge in edges:
            ranks[edge[1]] += 1
        
        result = []
        for i, r in enumerate(ranks):
            if not r:
                result.append(i)

        return result