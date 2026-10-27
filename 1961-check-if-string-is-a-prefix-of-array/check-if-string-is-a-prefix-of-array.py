class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        i, k = 0, 0

        while i < len(words) and k < len(s):
            if not s[k:].startswith(words[i]):
                return False

            k += len(words[i])
            i += 1
        
        return k >= len(s)