class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd, even, oe, eo, oec, eoc = 0, 0, 0, 0, 1, 0

        for n in nums:
            if n % 2 == 0:
                even += 1
                if oec == 0:
                    oe += 1
                    oec = 1
                if eoc == 0:
                    eo += 1
                    eoc = 1
            else:
                odd += 1
                if oec == 1:
                    oe += 1
                    oec = 0
                if eoc == 1:
                    eo += 1
                    eoc = 0


        return max(odd, even, eo, oe)