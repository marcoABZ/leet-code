class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result = []

        for word in words:
            result += [w for w in word.split(separator) if w]
        
        return result