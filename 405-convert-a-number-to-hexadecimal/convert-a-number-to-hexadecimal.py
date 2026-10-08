class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        if num < 0:
            num = 2**32 + num

        mapping = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        result = ""

        while num:
            if num % 16 >= 10:
                result = mapping[num % 16] + result
            else:
                result = str(num % 16) + result

            num //= 16
        
        return result
