class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        def toMorse(word):
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

            mp = {
                i: v for i, v in enumerate(morse)
            }
            result = ""
            for c in word:
                result += mp[ord(c) - ord('a')]
            
            return result
        
        return len(set([toMorse(word) for word in words]))