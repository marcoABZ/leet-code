class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = []
        d = []
        k = len(senate)

        for i, s in enumerate(senate):
            if s == 'R':
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            if r[0] < d[0]:
                r.append(k)
            else:
                d.append(k)
            
            r = r[1:]
            d = d[1:]
            k += 1

        return 'Radiant' if r else 'Dire'