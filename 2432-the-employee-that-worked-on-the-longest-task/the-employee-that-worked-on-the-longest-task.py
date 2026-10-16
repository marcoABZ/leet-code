from collections import defaultdict

class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        curr = 0
        top = 0
        topId = None

        for l in logs:
            duration = l[1] - curr
            if duration > top:
                top = duration
                topId = l[0]
            elif duration == top:
                topId = min(topId, l[0])
            curr = l[1]
        
        return topId