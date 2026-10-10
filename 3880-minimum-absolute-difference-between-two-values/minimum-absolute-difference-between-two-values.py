class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1, l2 = None, None
        mx = None

        for i, n in enumerate(nums):
            if n == 1:
                l1 = i
                if l2 is not None:
                    mx = l1 - l2 if mx is None else min(mx, l1 - l2)
            elif n == 2:
                l2 = i
                if l1 is not None:
                    mx = l2 - l1 if mx is None else min(mx, l2 - l1)
            
        return -1 if mx is None else mx