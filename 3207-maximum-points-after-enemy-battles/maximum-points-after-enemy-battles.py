import heapq

class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        """
        :type enemyEnergies: List[int]
        :type currentEnergy: int
        :rtype: int
        """
        points = 0

        mn = min(enemyEnergies)

        if currentEnergy < mn:
            return 0
        
        currentEnergy += sum(enemyEnergies) - mn
        return currentEnergy // mn