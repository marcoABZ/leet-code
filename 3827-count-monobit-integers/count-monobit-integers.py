class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        
        power = 0
        curr = 0
        result = 0
    
        while curr <= n:
            result += 1
            curr += 2 ** power
            power += 1
        
        return result