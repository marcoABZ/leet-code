class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        pos = 0
        sub = 0

        for m in moves:
            if m == 'R':
                pos += 1
            elif m == 'L':
                pos -= 1
            else:
                sub += 1

        return abs(pos) + sub