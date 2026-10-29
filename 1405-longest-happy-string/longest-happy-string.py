import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(pq)

        result = ""
        while True:
            count, char = heapq.heappop(pq)
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                nxtCount, nxtChar = heapq.heappop(pq)
                heapq.heappush(pq, (count, char))
                count, char = nxtCount, nxtChar

            if count == 0:
                break
            
            result += char
            heapq.heappush(pq, (count+1, char))
        
        return result