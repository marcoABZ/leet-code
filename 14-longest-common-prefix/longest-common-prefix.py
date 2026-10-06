class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        top = min([len(s) for s in strs])
        i = 0

        while i < top:
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]
            i += 1
        
        return strs[0][:i]
        