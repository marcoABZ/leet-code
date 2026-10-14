class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        p = directions[0]
        result = 0
        i = 1
        moving = 1 if directions[0] == 'R' else 0

        while i < len(directions):
            if p == 'R' and directions[i] == 'L':
                result += 2 + moving - 1
                moving = 0
                p = 'S'
            elif p == 'S' and directions[i] == 'L':
                result += 1
            elif p == 'R' and directions[i] == 'S':
                result += 1 + moving - 1
                moving = 0
                p = 'S'
            else:
                p = directions[i]
                if directions[i] == 'R':
                    moving += 1

            i += 1
        
        return result

