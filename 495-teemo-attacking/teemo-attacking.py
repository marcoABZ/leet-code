class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        currStart, currEnd = None, None
        total = 0

        for t in timeSeries:
            if currStart is None:
                currStart= t
                currEnd = t + duration
                continue
            
            if t <= currEnd:
                currEnd = t + duration
            else:
                total += currEnd - currStart
                currStart = t
                currEnd = t + duration

        return total + (currEnd - currStart)