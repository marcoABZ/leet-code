class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        result = 0

        while num:
            if num % 2 == 0:
                result += 2 ** i
            i += 1
            num >>= 1
        
        return result