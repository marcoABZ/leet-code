class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if k >= len(skills):
            return skills.index(max(skills))

        currSkill, currId, seq = skills[0], 0, 0

        queue = [(s, i+1) for i,s in enumerate(skills[1:])]
        while True:
            oponent, idOp = queue.pop(0)

            if currSkill > oponent:
                seq += 1
                queue.append((oponent, idOp))
            else:
                queue.append((currSkill, currId))
                currSkill, currId = oponent, idOp
                seq = 1
            
            if seq >= k:
                return currId
