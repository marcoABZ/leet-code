class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        i, j = startIndex - 1, (startIndex + 1) % len(words)
        while startIndex - i < len(words):
            if words[i] == target or words[j] == target:
                return startIndex - i
            i -= 1
            j = (j + 1) % len(words)
        
        return -1