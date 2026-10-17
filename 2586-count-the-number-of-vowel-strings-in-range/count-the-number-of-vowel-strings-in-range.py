class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowel = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for w in words[left:right+1]:
            if w[0] in vowels and w[-1] in vowels:
                vowel += 1
        
        return vowel