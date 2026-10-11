class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        v, c = 0, 0

        for ch in s:
            if not ch.isalpha():
                continue

            if ch in ['a', 'e', 'i', 'o', 'u']:
                v += 1
            else:
                c += 1
        
        return 0 if not c else v // c
        