import heapq

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def getKey(x):
            digits = []
            
            n = x
            while n:
                digits.append(n % 10)
                n //= 10
            
            digits.sort(reverse=True)
            n1 = 0
            for d in digits:
                n1 *= 10
                n1 += d
            
            return n1 - x

        start = sum(nums)
        pq = []

        for n in nums:
            if len(pq) < k:
                heapq.heappush(pq, getKey(n))
                continue
            
            key = getKey(n)
            if key > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, key)
        
        return start + sum(pq)

