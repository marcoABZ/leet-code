class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False

        for c in s:
            if c == 'b':
                foundB = True
            elif c == 'a':
                if foundB:
                    return False
        
        return True