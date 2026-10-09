class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        multiple = None

        while n:
            if multiple is None:
                multiple = (n % 2) == 0
            elif multiple and (n % 2) == 0:
                return False
            elif not multiple and (n % 2) == 1:
                return False
            
            multiple = (n % 2) == 0
            n //= 2
        
        return True