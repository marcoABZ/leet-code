class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        buckets = dict()

        for n in arr:
            if n in buckets:
                buckets[n] += 1
            else:
                buckets[n] = 1
        
        for n in target:
            if n not in buckets:
                return False
            buckets[n] -= 1
        
        return all([n == 0 for n in buckets.values()])