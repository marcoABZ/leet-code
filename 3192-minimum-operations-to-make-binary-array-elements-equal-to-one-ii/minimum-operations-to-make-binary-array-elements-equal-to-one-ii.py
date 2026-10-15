class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0

        for n in nums:
            if (ops % 2 == 0 and n == 0) or (ops % 2 == 1 and n == 1):
                ops += 1
        
        return ops