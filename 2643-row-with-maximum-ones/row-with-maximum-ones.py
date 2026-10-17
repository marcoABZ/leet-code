class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        top = 0
        row = 0

        for i, r in enumerate(mat):
            if sum(r) > top:
                top = sum(r)
                row = i
            
        return [row, top]