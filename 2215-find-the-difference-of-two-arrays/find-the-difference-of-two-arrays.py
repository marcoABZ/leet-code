class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set_a = set(nums1)
        set_b = set(nums2)

        return [list(set_a - set_b), list(set_b - set_a)]
        