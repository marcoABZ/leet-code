class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = 0
        rotations = 0

        for c in s:
            rotations += min(abs(int(c) - pos), pos + (9 - int(c) + 1), (9 - pos + 1) + int(c))
            pos = int(c)

        return rotations 