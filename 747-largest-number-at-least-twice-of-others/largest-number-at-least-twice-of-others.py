class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, second = max(nums[:2]), min(nums[:2])
        index = 0 if nums[0] > nums[1] else 1

        for i, n in enumerate(nums[2:]):
            if n >= largest:
                index = i + 2
                largest, second = n, largest
            elif n > second:
                second = n
        
        return index if largest >= 2 * second else -1