import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        i, j = 1, max(piles)

        while i < j:
            rate = i + (j - i) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / rate)
            
            if time <= h:
                j = rate
            else:
                i = rate + 1
        
        return i

        