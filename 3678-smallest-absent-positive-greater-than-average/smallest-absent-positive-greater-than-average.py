class Solution(object):
    def smallestAbsent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        avg = sum(nums) / len(nums)
        st = set(nums)
        c = max(1, avg + 1)

        while c in st:
            c += 1
        
        return c
