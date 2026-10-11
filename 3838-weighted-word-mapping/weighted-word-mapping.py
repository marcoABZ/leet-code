class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = ""

        for w in words:
            score = 0
            for c in w:
                score += weights[ord(c) - ord('a')]
            
            result += chr(ord('a') + abs((score % 26) - 25))
        return result