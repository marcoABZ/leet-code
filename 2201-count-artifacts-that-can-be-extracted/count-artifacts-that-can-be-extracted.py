class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        dig = set([(i, j) for i, j in dig])

        result = 0
        for artifact in artifacts:
            i1, j1, i2, j2 = artifact
            valid = True

            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    if (i, j) not in dig:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                result += 1
        
        return result
                    