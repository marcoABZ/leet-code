class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0

        while j < len(nums):
            if i != 0 and j < i and j % 2 == 0:
                j += 1
                continue
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                continue
            j += 1
        
        return nums