class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        curr = 0
        top = 0

        for g in gain:
            curr += g
            top = max(top, curr)
        
        return top