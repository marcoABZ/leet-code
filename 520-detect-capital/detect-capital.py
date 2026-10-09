class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return all([c.isupper() for c in word]) or all([c.islower() for c in word]) or (word[0].isupper() and not any([c.isupper() for c in word[1:]]))
        