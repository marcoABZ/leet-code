class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        return all([n % 2 == 0 for n in nums1]) or any([n % 2 == 1 for n in nums1])