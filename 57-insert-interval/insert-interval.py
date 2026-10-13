class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
    
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval] 

        i, j = 0, len(intervals) - 1
        while i <= j:
            mid = i + (j-i) // 2

            if intervals[mid][1] >= newInterval[0]:
                j = mid - 1
            else:
                i = mid + 1
        start = i

        i, j = 0, len(intervals) - 1
        while i <= j:
            mid = i + (j-i) // 2

            if intervals[mid][0] > newInterval[1]:
                j = mid - 1
            else:
                i = mid + 1
        end = i
        
        #print(start, end)

        return intervals[:start] + [[min(intervals[start][0], newInterval[0]), max(intervals[end-1][1], newInterval[1])]] + intervals[end:]