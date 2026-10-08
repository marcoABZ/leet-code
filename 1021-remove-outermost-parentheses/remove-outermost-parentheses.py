class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, 1
        balance = 1
        result = ""

        while j < len(s):
            if s[j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                result += s[i+1:j]
                i = j+1
                j += 1
                balance = 1

            j += 1

        return result
