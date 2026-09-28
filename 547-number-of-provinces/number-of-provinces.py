class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node, adj_matrix, visited):
            visited.add(node)
    
            for k, adjacent in enumerate(adj_matrix[node]):
                if adjacent and not k in visited:
                    dfs(k, adj_matrix, visited)
        
        provinces = 0
        inProvince = set()
        
        for i in range(len(isConnected)):
            if i in inProvince:
                continue

            provinces += 1
            dfs(i, isConnected, inProvince)

        return provinces