class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for n in nums:
            if n % 2 == 0:
                result |= n
        
        return result