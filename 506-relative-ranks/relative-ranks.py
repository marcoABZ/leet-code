class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ranks = sorted([(v, i) for i, v in enumerate(score)], reverse = True)

        answer = [0] * len(score)
        for i, pos in enumerate(ranks):
            if i == 0:
                answer[pos[1]] = "Gold Medal"
            elif i == 1:
                answer[pos[1]] = "Silver Medal"
            elif i == 2:
                answer[pos[1]] = "Bronze Medal"
            else:
                answer[pos[1]] = str(i+1)
        
        return answer
