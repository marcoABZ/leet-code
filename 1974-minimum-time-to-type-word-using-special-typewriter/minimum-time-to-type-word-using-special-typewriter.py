class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 0
        time = 0

        for c in word:
            idx = ord(c) - ord('a')

            dist = None
            if idx > curr:
                dist = min(curr + 26 - idx, idx - curr)
            else:
                dist = min(26 - curr + idx, curr - idx)
            
            curr = idx
            time += dist + 1
        
        return time