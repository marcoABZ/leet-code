class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sums = dict()

        for i, s in enumerate(list1):
            sums[s] = (i, s, False)
        
        for i, s in enumerate(list2):
            if s in sums:
                sums[s] = (sums[s][0] + i, s, True)
        
        values = sorted([s for s in sums.values() if s[2]])
        i = 0
        result = []

        while i < len(values) and values[i][0] == values[0][0]:
            result.append(values[i][1])
            i += 1
    
        return result
        