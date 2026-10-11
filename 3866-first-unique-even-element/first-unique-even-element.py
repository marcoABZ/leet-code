class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}

        for i, n in enumerate(nums):
            if n % 2 == 1:
                continue

            if n not in counter:
                counter[n] = (1, i)
            else:
                counter[n] = (False, i)
        
        candidates = sorted([(k, v[1]) for k, v in counter.items() if v[0]], key=lambda x: x[1])
        return -1 if not candidates else candidates[0][0]
