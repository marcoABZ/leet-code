class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = 0

        for n in nums1:
            for m in nums2:
                if n % (m * k) == 0:
                    pairs += 1
        
        return pairs