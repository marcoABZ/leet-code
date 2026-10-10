class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        top = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                top = max(top, (nums[i] * nums[j]) / (gcd(nums[i], nums[j]) ** 2))
        
        return top