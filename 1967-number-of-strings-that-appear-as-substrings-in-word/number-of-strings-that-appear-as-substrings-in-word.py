class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        def isSubstring(s, target):
            i, j = 0, len(s)

            while j <= len(target):
                if target[i:j] == s:
                    return True
                i += 1
                j += 1
            
            return False
        
        result = 0
        for w in patterns:
            if isSubstring(w, word):
                result += 1
        
        return result