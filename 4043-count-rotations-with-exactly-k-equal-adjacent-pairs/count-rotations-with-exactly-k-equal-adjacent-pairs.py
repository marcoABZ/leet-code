class Solution(object):
    def countRotations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        equals = 0
        for i in range(len(s)):
            if s[i-1] == s[i]:
                equals += 1
        
        if k == equals - 1:
            return equals
        elif k == equals:
            return len(s) - equals
        return 0