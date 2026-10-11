class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurences = dict()
        mn = -1

        for i, n in enumerate(nums):
            if n in occurences:
                occurences[n].append(i)
                if len(occurences[n]) >= 3:
                    distance = 2 * (i - occurences[n][-3])
                    mn = distance if mn == - 1 else min(mn, distance)
            else:
                occurences[n] = [i]

        return mn 