from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)

        return c.most_common()[0][1] <= 2