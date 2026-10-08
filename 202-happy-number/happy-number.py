class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while True:
            newNumber = 0
            if n in seen:
                return False
            if n == 1:
                return True

            seen.add(n)
            while n:
                newNumber += (n % 10) ** 2
                n //= 10
            n = newNumber
        