class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        
        if i >= j:
            return True
        
        k, l, m, n = i, j-1, i+1, j
        
        while k < l:
            if s[k] != s[l]:
                break
            k += 1
            l -= 1
        
        if k >= l:
            return True
        
        while m < n:
            if s[m] != s[n]:
                return False
            m += 1
            n -= 1
        return True