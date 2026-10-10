class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd, even = 0, 0
        ans = []

        for n in nums[::-1]:
            if n % 2 == 0:
                even += 1
                ans.insert(0, odd)
            else:
                odd += 1
                ans.insert(0, even)
        
        return ans