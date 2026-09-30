class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ranks = [[0,0] for _ in range(n)]

        for a, b in trust:
            ranks[a-1][0] += 1
            ranks[b-1][1] += 1

        for i,r in enumerate(ranks):
            if r[0] == 0 and r[1] == n-1:
                return i + 1
        return -1

        