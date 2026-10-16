class Solution:
    def oddString(self, words: list[str]) -> str:
        seen = dict()
        for i, word in enumerate(words):
            diff = tuple([ord(w) - ord(word[i]) for i, w in enumerate(word[1:])])

            if not seen:
                seen[diff] = i
            else:
                if diff not in seen:
                    if i != 1:
                        return word
                    seen[diff] = i
                else:
                    if len(seen.values()) > 1:
                        del seen[diff]
                        return words[list(seen.values())[0]]
