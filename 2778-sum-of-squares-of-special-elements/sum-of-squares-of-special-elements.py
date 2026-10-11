class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        size = len(nums)

        for i, n in enumerate(nums):
            if size % (i + 1) == 0:
                total += n ** 2
            
        return total