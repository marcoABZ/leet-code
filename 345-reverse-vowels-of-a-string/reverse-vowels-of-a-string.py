class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        i, j = 0, len(s) - 1
        while i < len(s) and s[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
            i += 1
        while j >= 0 and s[j].lower() not in ['a', 'e', 'i', 'o', 'u']:
            j -= 1

        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

            while i < j and s[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                i += 1
            while j > i and s[j].lower() not in ['a', 'e', 'i', 'o', 'u']:
                j -= 1
        
        return "".join(chars)