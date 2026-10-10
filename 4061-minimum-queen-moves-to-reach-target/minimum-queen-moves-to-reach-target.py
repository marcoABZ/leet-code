class Solution(object):
    def minQueenMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        if source == target:
            return 0
        elif (abs(source[0] - target[0]) == abs(source[1] - target[1])) or (target[0] == source[0]) or (target[1] == source[1]):
            return 1
        return 2