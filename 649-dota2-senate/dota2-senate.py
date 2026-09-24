class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue = [c for c in senate]
        r, d = 0, 0
        
        while 'D' in queue and 'R' in queue:
            curr = queue[0]
            queue = queue[1:]
            if curr == 'R':
                if r < 0:
                    r += 1
                else:
                    d -= 1
                    queue.append(curr)
            else:
                if d < 0:
                    d += 1
                else:
                    r -= 1
                    queue.append(curr)


        return 'Radiant' if queue[0] == 'R' else 'Dire'