class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        ones = 0
        movable = False

        for c in s:
            if c == "1":
                ones += 1
                movable = True
            elif movable:
                result += ones
                movable = False
        
        return result