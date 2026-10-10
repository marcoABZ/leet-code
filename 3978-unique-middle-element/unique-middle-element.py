class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = len(nums) // 2
        middle = nums[idx]

        for i, n in enumerate(nums):
            if i == idx:
                continue
            if n == middle:
                return False
        
        return True
        