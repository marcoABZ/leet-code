class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        top = 0

        for s in strs:
            try:
                top = max(top, int(s))
            except:
                top = max(top, len(s))
        
        return top