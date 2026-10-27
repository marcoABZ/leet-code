class Solution:
    def makeFancyString(self, s: str) -> str:
        ch = s[0]
        repeat = 1

        result = s[0]

        for c in s[1:]:
            if c == ch:
                repeat += 1
            else:
                repeat = 1
                ch = c
            
            if repeat < 3:
                result += c
        
        return result