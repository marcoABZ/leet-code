class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m * n:
            return []

        result = [[0] * n for _ in range(m)]

        for i, v in enumerate(original):
            result[i // n][i % n] = v
        
        return result