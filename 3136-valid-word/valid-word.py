class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowel, consonant = False, False
        for c in word:
            if not c.isalnum():
                return False
            elif c.isdigit():
                continue

            if c.lower() in ["a", "e", "i", "o", "u"]:
                vowel = True
            else:
                consonant = True
        
        return vowel and consonant