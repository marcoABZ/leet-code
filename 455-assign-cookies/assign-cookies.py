class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        i, j, result = 0, 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                result += 1
                j += 1
            i += 1

        return result