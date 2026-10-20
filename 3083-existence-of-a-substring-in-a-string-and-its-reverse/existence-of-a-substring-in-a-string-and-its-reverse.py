class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        target = set()

        for i in range(1, len(s)):
            if s[i] + s[i-1] in target or s[i-1] == s[i]:
                return True
            
            target.add(s[i-1:i+1])
        
        return False