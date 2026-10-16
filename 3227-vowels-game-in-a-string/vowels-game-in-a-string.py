class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 0
        st = set(['a', 'e', 'i', 'o', 'u'])

        for c in s:
            if c in st:
                return True
        
        return False