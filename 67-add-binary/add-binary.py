class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i, j, carry = len(a) - 1, len(b) - 1, 0
        result = ""

        while i >= 0 and j >= 0:
            total = int(a[i]) + int(b[j]) + carry
            carry = total // 2

            result = str(total % 2) + result
            i -= 1
            j -= 1
        
        while i >= 0:
            total = int(a[i]) + carry
            carry = total // 2

            result = str(total % 2) + result
            i -= 1
        
        while j >= 0:
            total = int(b[j]) + carry
            carry = total // 2

            result = str(total % 2) + result
            j -= 1
        
        if carry:
            result = str(carry) + result
        
        return result
