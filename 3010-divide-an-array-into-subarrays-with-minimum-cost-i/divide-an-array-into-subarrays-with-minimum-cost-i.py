class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = nums[0]
        m, s = 51, 51

        for n in nums[1:]:
            if n <= m:
                s = m
                m = n
            elif n < s:
                s = n

        return f + m + s 