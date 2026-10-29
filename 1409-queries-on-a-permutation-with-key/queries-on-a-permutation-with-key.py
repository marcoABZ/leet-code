class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = [i + 1 for i in range(m+1)]
        
        result = []
        for q in queries:
            for i, v in enumerate(p):
                if v == q:
                    p = [q] + p[:i] + p[i+1:]
                    result.append(i)
        
        return result