class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counter = {}

        for w in arr:
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 1
        
        distinct = 0
        for w in arr:
            if counter[w] == 1:
                distinct += 1
                if distinct == k:
                    return w
        
        return ""
        