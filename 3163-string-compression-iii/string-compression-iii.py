class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        result = ""

        for i, c in enumerate(word[1:]):
            if c == word[i]:
                count += 1
                if count > 9:
                    result += "9" + c
                    count = 1
            else:
                result += str(count) + word[i]
                count = 1

        result += str(count) + word[-1]
        return result
                
