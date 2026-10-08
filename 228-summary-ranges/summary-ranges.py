class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        i, j = 0, 1
        result = []

        while j < len(nums):
            if nums[j] == nums[j-1] + 1:
                j += 1
                continue
            
            if j == i + 1:
                result.append(str(nums[i]))
            else:
                result.append(str(nums[i]) + "->" + str(nums[j-1]))
            
            i = j
            j += 1
    
        if j == i + 1:
            result.append(str(nums[i]))
        else:
            result.append(str(nums[i]) + "->" + str(nums[j-1]))
        return result
        