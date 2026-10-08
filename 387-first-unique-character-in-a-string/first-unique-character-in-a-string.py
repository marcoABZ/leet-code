class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = dict()

        for i,c in enumerate(s):
            if c in counter:
                counter[c] = -1
            else:
                counter[c] = i
        
        valid = [v for v in counter.values() if v != -1]
        if not valid:
            return -1
        return min(valid)