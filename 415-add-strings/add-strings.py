class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j, carry = len(num1)-1, len(num2)-1, 0
        result = ""

        while i >= 0 and j >= 0:
            tot = int(num1[i]) + int(num2[j]) + carry
            carry = tot // 10
            result = str(tot % 10) + result

            i -= 1
            j -= 1
        
        while i >= 0 and carry:
            tot = int(num1[i]) + carry
            carry = tot // 10
            result = str(tot % 10) + result

            i -= 1
        if i >= 0:
            result = num1[:i+1] + result
        
        while j >= 0 and carry:
            tot = int(num2[j]) + carry
            carry = tot // 10
            result = str(tot % 10) + result

            j -= 1
        if j >= 0:
            result = num2[:j+1] + result
        
        if carry:
            result = "1" + result
        return result