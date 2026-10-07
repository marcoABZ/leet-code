class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0

        for i, n in enumerate(arr):
            total += n
            if i != 0: arr[i] += arr[i-1]

            j = i - 2
            while j > 0:
                total += arr[i] - arr[j-1]
                j -= 2
            
            if j == 0:
                total += arr[i]
        
        return total