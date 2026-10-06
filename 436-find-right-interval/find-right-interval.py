class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_ints = sorted([(v, i) for i, v in enumerate(intervals)], key=lambda x: x[0])
        result = [-1] * len(intervals)

        for i, interval in enumerate(sorted_ints):
            best = -1
            lo, hi = i, len(sorted_ints) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if sorted_ints[mid][0][0] >= interval[0][1]:
                    hi = mid - 1
                    best = sorted_ints[mid][1]
                else:
                    lo = mid + 1
            
            result[interval[1]] = best
        
        return result
