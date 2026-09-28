class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_points = sorted(points)
        i = 0
        arrows = 0

        while i < len(sorted_points):
            curr = sorted_points[i]
            j = i + 1
            limit = curr[1]
            while j < len(sorted_points) and limit >= sorted_points[j][0]:
                limit = min(limit, sorted_points[j][1])
                j += 1

            i = j
            arrows += 1

        return arrows