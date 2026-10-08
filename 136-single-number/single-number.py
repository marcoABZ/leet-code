class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()

        for n in nums:
            if n in count:
                del count[n]
            else:
                count[n] = True
        
        return count.keys()[0]
        