class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        toDelete = 0
        for i in range(len(strs[0])):
            values = [ord(s[i]) for s in strs]
            for j in range(1, len(values)):
                if values[j] < values[j-1]:
                    toDelete += 1
                    break

        return toDelete