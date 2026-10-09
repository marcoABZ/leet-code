class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = dict()
        arrDegree = 0

        for i, n in enumerate(nums):
            if n in counts:
                degree, first, last = counts[n]
                counts[n] = (degree + 1, first, i)
            else:
                counts[n] = (1, i, i)
            
            arrDegree = max(arrDegree, counts[n][0])
        
        valid = [v[2]-v[1]+1 for v in counts.values() if v[0] == arrDegree]
        return min(valid)
         