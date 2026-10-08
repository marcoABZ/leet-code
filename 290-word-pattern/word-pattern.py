class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = [w for w in s.split(" ") if w]
        mappings_p = dict()
        mappings_w = dict()

        if len(pattern) != len(words):
            return False
        
        for i, c in enumerate(pattern):
            if c not in mappings_p:
                mappings_p[c] = words[i] 
            elif mappings_p[c] != words[i]:
                return False
            
            if words[i] not in mappings_w:
                mappings_w[words[i]] = c
            elif mappings_w[words[i]] != c:
                return False

        return True
