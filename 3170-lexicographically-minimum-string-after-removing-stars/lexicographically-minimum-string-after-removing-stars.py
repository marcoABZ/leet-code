import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        pq = []

        for i, c in enumerate(s):
            if c == '*':
                heapq.heappop(pq)
            else:
                heapq.heappush(pq, (ord(c), len(s)-i))
        
        return "".join([chr(k[0]) for k in sorted(pq, key=lambda x: x[1], reverse=True)])
