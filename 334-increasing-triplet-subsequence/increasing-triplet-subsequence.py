class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        i, j, k = 0, 1, None
        while j < len(nums) and (k == None or k < len(nums)):
            if not k:
                if nums[j] < nums[i]:
                    i = j
                    j += 1
                elif nums[j] > nums[i]:
                    k = j+1
                else:
                    j += 1
            else:
                if nums[k] < nums[j] and nums[k] < nums[i]:
                    i = k
                    k += 1
                elif nums[k] < nums[j] and nums[k] > nums[i]:
                    j = k
                    k += 1
                elif nums[k] > nums[j]:
                    return True
                else:
                    k += 1
        
        return False
