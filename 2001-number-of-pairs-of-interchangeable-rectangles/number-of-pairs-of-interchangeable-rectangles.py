class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        ratios = sorted([float(r[0]) / r[1] for r in rectangles])

        i, j, result = 0, 0, 0
        while j < len(ratios):
            if ratios[j] == ratios[i]:
                j += 1
            else:
                result += (j-i) * (j-i-1) / 2
                i = j
        
        result += (j-i) * (j-i-1) / 2
        return int(result)