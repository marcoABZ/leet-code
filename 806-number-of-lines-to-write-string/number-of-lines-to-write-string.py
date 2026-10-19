class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        currLine = 0

        for c in s:
            cWidth = widths[ord(c) - ord('a')]
            currLine += cWidth

            if currLine > 100:
                lines += 1
                currLine = cWidth
        
        return [lines, currLine]