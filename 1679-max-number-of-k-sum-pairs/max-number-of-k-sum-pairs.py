class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        st = sorted(nums)
        i, j = 0, len(st) - 1
        result = 0

        while i < j:
            curr = st[i] + st[j]
            if curr == k:
                i += 1
                j -= 1
                result += 1
            elif curr < k:
                i += 1
            else:
                j -= 1
        
        return result