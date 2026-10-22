class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        broken = set(list(brokenLetters))
        result = 0

        for word in words:
            valid = True
            
            for c in word:
                if c in broken:
                    valid = False
                    break
            
            if valid: result += 1
        
        return result