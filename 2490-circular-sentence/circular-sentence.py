class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        words.append(words[0])

        for i in range(1, len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
        
        return True