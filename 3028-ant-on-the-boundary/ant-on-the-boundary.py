class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        returns = 0

        for n in nums:
            pos += n

            if pos == 0:
                returns += 1
        
        return returns