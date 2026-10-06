class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a, b = s[len(s) // 2:], s[:len(s) // 2]

        vowels = 0
        for c in a:
            if c.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
        
        for c in b:
            if c.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels -= 1
        
        return vowels == 0