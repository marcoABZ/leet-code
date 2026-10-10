class Solution(object):
    def rearrangeString(self, s, x, y):
        """
        :type s: str
        :type x: str
        :type y: str
        :rtype: str
        """
        counter = {
            x: 0,
            y: 0
        }
        remaining = ""

        for c in s:
            if c == x or c == y:
                counter[c] += 1
            else:
                remaining += c
        
        return counter[y] * y + counter[x] * x + remaining