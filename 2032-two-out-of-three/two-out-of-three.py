class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        vals = set()
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)

        vals |= (nums1 & nums2)
        vals |= (nums2 & nums3)
        vals |= (nums1 & nums3)

        return list(vals)