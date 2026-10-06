class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        i, best = 0, 0
        while i < len(forts) and forts[i] == 0:
            i += 1

        if i == len(forts):
            return 0
            
        j, start = i+1, forts[i]

        while j < len(forts):
            if forts[j] == 0:
                j += 1
                continue

            if (start == 1 and forts[j] == -1) or (start == -1 and forts[j] == 1):
                best = max(best, j-i-1)
            
            i = j
            start = forts[j]
            j += 1
        
        return best