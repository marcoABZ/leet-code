class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        mx, diag = 0, 0

        for d in dimensions:
            dg = (d[0] * d[0] + d[1] * d[1]) ** 0.5
            if dg > diag:
                diag = dg
                mx = d[0] * d[1]
            elif dg == diag:
                mx = max(mx, d[0] * d[1])
        
        return mx