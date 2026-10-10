class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i, j = 0, len(s)
        result = []

        for c in s:
            if c == "I":
                result.append(i)
                i += 1
            else:
                result.append(j)
                j -= 1
        
        result.append(i)
        return result