class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        found = False
        for i, c in enumerate(word):
            if c == ch:
                found = True
                break
        
        if not found:
            return word
        return word[0:i+1][::-1] + word[i+1:]