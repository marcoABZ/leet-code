from collections import defaultdict

class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ranges = defaultdict(int)
        maxRange = -1

        for num in nums:
            mn, mx, n = 10, -1, num
            
            while n:
                mn = min(mn, n % 10)
                mx = max(mx, n % 10)
                n //= 10
            
            ranges[mx-mn] += num
            maxRange = max(maxRange, mx-mn)
        
        return ranges[maxRange]

