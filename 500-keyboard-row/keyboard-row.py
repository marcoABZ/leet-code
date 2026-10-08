class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rowMap = dict()
        for l in list("qwertyuiop"):
            rowMap[l] = 1
        for l in list("asdfghjkl"):
            rowMap[l] = 2
        for l in list("zxcvbnm"):
            rowMap[l] = 3

        result = []
        for word in words:
            row = rowMap[word[0].lower()]
            ok = True
            for c in word[1:].lower():
                if rowMap[c] != row:
                    ok = False
                    break
            if ok:
                result.append(word)
        
        return result
