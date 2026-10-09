class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        values = {
            l: i for i, l in enumerate(list(order))
        }

        def inLexical(w1, w2, values):
            i, j = 0, 0

            while i < len(w1) and j < len(w2):
                if values[w1[i]] == values[w2[j]]:
                    i += 1
                    j += 1
                else:
                    return values[w1[i]] < values[w2[j]]
            
            return len(w1) <= len(w2)
                
        for i in range(1, len(words)):
            if not inLexical(words[i-1], words[i], values):
                return False
        return True