class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        diffIdx = []
        letters = set()
        repeated = False

        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffIdx.append(i)
                if len(diffIdx) > 2:
                    return False
            if s[i] in letters:
                repeated = True
            letters.add(s[i])
        
        if not diffIdx:
            return repeated
        if len(diffIdx) == 1:
            return False
        i, j = diffIdx
        return s[i] == goal[j] and s[j] == goal[i]