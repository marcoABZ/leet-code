class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            newNum = 0

            while num:
                newNum += num % 10
                num //= 10
            num = newNum

        return num
