class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = [w for w in sentence.split(" ") if w]

        valid = 0
        for w in words:
            if w[0] == "-" or w[-1] == "-":
                continue
            
            v = True
            hiphens = 0
            for i, c in enumerate(w):
                if (c in [",", "!", "."] and i != len(w)-1) or c.isdigit():
                    v = False
                    break

                if c == "-":
                    hiphens += 1
                    if hiphens > 1 or (not w[i-1].isalpha() or not w[i+1].isalpha()):
                        v = False
                        break

            if v:
                print(w)
                valid += 1
        
        return valid