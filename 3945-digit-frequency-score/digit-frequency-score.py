from collections import defaultdict

class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = defaultdict(int)

        while n:
            count[n % 10] += 1
            n //= 10
        
        return sum([k * v for k, v in count.items()])