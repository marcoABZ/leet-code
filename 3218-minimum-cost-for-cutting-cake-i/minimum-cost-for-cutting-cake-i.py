class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        v, h = 1, 1
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        i, j = 0, 0
        result = 0

        while i < len(horizontalCut) or j < len(verticalCut):
            vc = 0 if j >= len(verticalCut) else verticalCut[j]
            hc = 0 if i >= len(horizontalCut) else horizontalCut[i]

            if vc > hc:
                result += vc * h
                v += 1
                j += 1
            else:
                result += hc * v
                h += 1
                i += 1
        
        return result
