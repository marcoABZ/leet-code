class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        nums1 = set(nums1)
        result = 100

        for n in nums2:
            if n in nums1:
                result = min(result, n)
        
        if result < 10:
            return result
        v1, v2 = min(nums1), min(nums2)

        if v1 < v2:
            return 10 * v1 + v2
        return 10 * v2 + v1