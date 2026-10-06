class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        rows = {i: set() for i in range(n)}
        cols = {j: set() for j in range(n)}

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell in rows[i] or cell in cols[j]:
                    return False

                rows[i].add(cell)
                cols[j].add(cell)

        return True