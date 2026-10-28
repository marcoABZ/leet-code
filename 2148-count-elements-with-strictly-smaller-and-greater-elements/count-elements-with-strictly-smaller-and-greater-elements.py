from collections import Counter

class Solution:
    def countElements(self, nums: list[int]) -> int:
        c = Counter(nums)
        return max(0, len(nums) - c[max(nums)] - c[min(nums)])