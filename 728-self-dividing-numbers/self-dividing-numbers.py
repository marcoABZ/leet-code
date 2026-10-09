class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(n):
            a = n
            while a:
                if not (a % 10) or (n % (a % 10)) != 0:
                    return False
                a //= 10
            return True
        
        return [i for i in range(left, right+1) if isSelfDividing(i)]