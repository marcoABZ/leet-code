class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals)
        end = intervals[0][1]
        i = 1
        result = 0

        while i < len(intervals):
            if end > intervals[i][0]:
                result += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
            i += 1
        
        return result
        