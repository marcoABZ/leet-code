class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        p = [i + 1 for i in range(m+1)]
        
        result = []
        for q in queries:
            for i, v in enumerate(p):
                if v == q:
                    p.pop(i)
                    p.insert(0, v)
                    result.append(i)
        
        return result