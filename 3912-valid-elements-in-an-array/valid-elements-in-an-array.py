class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maxr, maxl = [0], [0]

        for i, n in enumerate(nums):
            maxl.append(max(maxl[i], n))
        
        for i, n in enumerate(nums[::-1]):
            maxr.insert(0, max(maxr[0], n))
        
        result = []

        for i, n in enumerate(nums):
            if n > maxl[i] or n > maxr[i+1]:
                result.append(n)
        
        return result

