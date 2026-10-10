class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j = len(nums) - 1

        while j >= 0:
            nums.append(nums[j])
            j -= 1

        return nums