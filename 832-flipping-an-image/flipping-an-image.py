class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def swap(i):
            if i == 0:
                return 1
            return 0
        
        return [[swap(i) for i in row[::-1]] for row in image]