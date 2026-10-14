class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j, k = 0, 1, 1

        while j < len(nums):
            if nums[i] == nums[j]:
                if j - i < 2:
                    nums[k] = nums[j]
                    k += 1
                j += 1

            else:
                i = j
                nums[k] = nums[j]
                k += 1
                j += 1
        
        return k
                    
            