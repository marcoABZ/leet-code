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
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            plants += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
    
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                plants += 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            plants += 1
        
        return plants >= n