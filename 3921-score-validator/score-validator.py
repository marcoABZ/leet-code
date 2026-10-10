class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        counter, score = 0, 0

        for ev in events:
            if ev in ["WD", "NB"]:
                score += 1
            elif ev == "W":
                counter += 1
                if counter == 10:
                    return [score, counter]
            else:
                score += int(ev)
        
        return [score, counter]