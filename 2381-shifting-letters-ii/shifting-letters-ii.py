class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        pos = [0] * (len(s)+1)

        for start, end, dir in shifts:
            if dir == 1:
                pos[start] += 1
                pos[end+1] -= 1
            else:
                pos[start] -= 1
                pos[end+1] += 1
        
        for i in range(len(pos)):
            if i > 0:
                pos[i] += pos[i-1]
            pos[i] %= 26
        
        result = ""
        for i, c in enumerate(s):
            endPos = ord(c) + pos[i]

            if endPos < ord('a'):
                result += chr(ord('z') - (ord('a') - endPos - 1))
            elif endPos > ord('z'):
                result += chr(ord('a') + (endPos - ord('z') - 1))
            else:
                result += chr(endPos)

        return result