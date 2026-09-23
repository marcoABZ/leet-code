class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = [0]
        total = 0

        for num in nums[::-1]:
            total += num
            right_sum.insert(0, total)
        
        total = 0
        for i, num in enumerate(nums):
            if total == right_sum[i+1]:
                return i
            total += num
        
        return -1
