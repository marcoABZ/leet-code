class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
    
        i, j = 0, len(nums)

        while i <= j:
            pos = i + (j - i) // 2

            if pos == 0: 
                if nums[0] > nums[1]:
                    return 0
                i = 1
                continue
            if pos == len(nums) - 1:
                if nums[-1] > nums[-2]:
                    return len(nums) - 1
                j = len(nums) - 2
                continue
            
            if nums[pos] > nums[pos-1] and nums[pos] > nums[pos+1]:
                return pos
            if nums[pos-1] > nums[pos]:
                j = pos - 1
            else:
                i = pos + 1
        
        return -1
