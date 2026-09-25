import math

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        result = []
        sorted_pots = sorted(potions)

        for s in spells:
            min_strength = math.ceil(float(success) / s)
            i, j = 0, len(sorted_pots)

            while i < j:
                mid = i + (j - i) // 2

                if sorted_pots[mid] >= min_strength:
                    j = mid
                else:
                    i = mid + 1
            
            result.append(len(sorted_pots) - i)
        
        return result