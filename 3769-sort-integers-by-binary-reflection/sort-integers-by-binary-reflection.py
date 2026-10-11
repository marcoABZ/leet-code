class Solution(object):
    def sortByReflection(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def reflection(num):
            val = 0

            while num:
                val <<= 1
                val += num % 2
                num >>= 1
            
            return val
        
        return sorted(nums, key=lambda x: (reflection(x), x))