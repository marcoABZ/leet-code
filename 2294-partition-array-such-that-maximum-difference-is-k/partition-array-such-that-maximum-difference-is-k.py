class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        subseq, j = 1, 0

        for i, n in enumerate(nums[1:]):
            if n - nums[j] > k:
                subseq += 1
                j = i + 1

        return subseq