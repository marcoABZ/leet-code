class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        types = set()

        for c in candyType:
            types.add(c)
        
        return min(len(types), len(candyType) // 2)