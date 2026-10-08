class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dist = 0
        while x or y:
            if x % 2 != y % 2:
                dist += 1
            
            x >>= 1
            y >>= 1
        
        return dist
        