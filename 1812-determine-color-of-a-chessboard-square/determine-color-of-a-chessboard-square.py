class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        value = int(ord(coordinates[0]) - ord('a')) + int(coordinates[1])

        return value % 2 == 0