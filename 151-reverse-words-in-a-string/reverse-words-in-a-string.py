class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [w for w in s.split(" ") if w]
        i, j = 0, len(words) - 1

        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        
        return " ".join(words)