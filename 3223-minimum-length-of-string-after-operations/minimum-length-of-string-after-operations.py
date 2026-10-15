from collections import defaultdict

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = defaultdict(int)
        result = len(s)

        for c in s:
            counter[c] += 1
            if counter[c] == 3:
                result -= 2
                counter[c] -= 2
        
        return result