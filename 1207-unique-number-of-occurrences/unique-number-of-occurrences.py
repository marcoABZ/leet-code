class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = {}

        for n in arr:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        return len(counter.values()) == len(set(counter.values()))
        