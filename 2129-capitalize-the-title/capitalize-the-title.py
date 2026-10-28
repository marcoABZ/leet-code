class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def capitalize(word):
            if len(word) <= 2:
                return word.lower()
            return word.capitalize()
        
        return " ".join([capitalize(word) for word in title.split(" ")])