class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        remaining = len(nums)
        dominants = 0

        for n in nums: 
            total -= n
            remaining -= 1
            if remaining and n > (total / float(remaining)):
                dominants += 1
        
        return dominants