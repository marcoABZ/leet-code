class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 0   (0)  1000 (1) 10000 (1) 11000 (2)
        # 1   (1)  1001 (2) 10001 (2) 11001 (3)
        # 10  (1)  1010 (2) 10010 (2) 11010 (3)
        # 11  (2)  1011 (3) 10011 (3) 11011 (4)
        # 100 (1)  1100 (2) 10100 (2) 11100 (3)
        # 101 (2)  1101 (3) 10101 (3) 11101 (4)
        # 110 (2)  1110 (3) 10110 (3) 11110 (4)
        # 111 (3)  1111 (4) 10111 (4) 11111 (5)
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        result = [0, 1]
        power = 1
        while 2 ** power <= n:
            sl = result[len(result) // 2:]
            result += sl
            result += [1 + i for i in sl]
            power += 1
        
        return result[:n+1]


        