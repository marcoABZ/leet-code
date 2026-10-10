class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        special = { nums[0]: True }
        curr = nums[0]

        for n in nums[1:]:
            if n == curr:
                continue
            
            if n in special:
                special[n] = False
            else:
                special[n] = True
            curr = n
        
        return len([v for v in special.values() if v])
