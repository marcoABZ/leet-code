class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        parts = [w for w in s.split(" ") if w]
        return len(parts[-1])
        