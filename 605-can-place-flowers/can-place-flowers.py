class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        if len(flowerbed) == 1:
            return flowerbed[0] == 0 and n <= 1
    
        plants = 0

        left = flowerbed[:]
        if left[0] == 0 and left[1] == 0:
            left[0] = 1
            plants += 1

        for i in range(1, len(flowerbed) - 1):
            if left[i] == 1:
                continue
    
            if left[i-1] == 0 and left[i+1] == 0:
                left[i] = 1
                plants += 1
        
        if left[-1] == 0 and left[-2] == 0:
            left[-1] = 1
            plants += 1
        
        return plants >= n