class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 1
        el = nums[0]
        count = 1

        for n in nums[1:]:
            if n == el and count >= k:
                continue
            
            nums[i] = n
            i += 1
            count = 1 if n != el else count + 1
            el = n
        
        return nums[:i]