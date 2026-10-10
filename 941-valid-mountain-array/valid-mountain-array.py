class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len < 3:
            return False
        
        descending = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] > arr[i-1] and descending:
                return False
            elif arr[i] < arr[i-1] and not descending:
                if i == 1:
                    return False
                else:
                    descending = True
        
        return descending