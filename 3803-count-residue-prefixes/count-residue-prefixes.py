class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct = set()
        residues = 0

        for i, c in enumerate(s):
            distinct.add(c)
            if len(distinct) >= 3:
                break
            
            if len(distinct) == (i+1) % 3:
                residues += 1
        
        return residues