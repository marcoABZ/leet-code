class Solution:
    def addMinimum(self, word: str) -> int:
        result = 0
        if word[0] == 'b':
            result += 1
        elif word[0] == 'c':
            result += 2

        for i, n in enumerate(word[1:]):
            if n == word[i]:
                result += 2
            elif n == 'a' and word[i] == 'b':
                result += 1
            elif n == 'b' and word[i] == 'c':
                result += 1
            elif n == 'c' and word[i] == 'a':
                result += 1
        
        if word[-1] == 'a':
            return result + 2
        elif word[-1] == 'b':
            return result + 1

        return result
    