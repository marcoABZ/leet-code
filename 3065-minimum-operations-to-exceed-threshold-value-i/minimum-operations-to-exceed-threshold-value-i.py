import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i, j = 0, len(nums)-1

        while i <= j:
            mid = i + (j-i) // 2

            if nums[mid] >= k:
                j = mid - 1
            else:
                i = mid + 1
        
        return i