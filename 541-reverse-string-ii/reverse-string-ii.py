class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i, j, l = 0, k, 2*k
        result = ""

        while l <= len(s):
            result += s[i:j][::-1] + s[j:l]
            i, j, l = l, l+k, l+2*k
        
        if i >= len(s):
            return result
        result += s[i:min(len(s),j)][::-1] + s[min(len(s),j):]
        return result