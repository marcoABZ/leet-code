class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        p = 0

        while n:
            pos = (n % 10) * (10 ** p)
            if pos:
                result.insert(0, pos)
            p += 1
            n //= 10
        
        return result