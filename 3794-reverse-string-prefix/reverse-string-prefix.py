class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        i, j = 0, k-1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)