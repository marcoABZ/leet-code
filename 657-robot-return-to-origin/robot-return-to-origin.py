class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h, v = 0, 0

        for m in moves:
            if m == 'U':
                v += 1
            elif m == 'D':
                v -= 1
            elif m == 'R':
                h += 1
            else:
                h -= 1
        
        return h == 0 and v == 0