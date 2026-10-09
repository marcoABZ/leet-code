class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        missing = 0
        balance = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                balance += 1
                i += 1
            elif s[i] == ')':
                balance -= 1
                if i == len(s) - 1:
                    missing += 1
                    i += 1
                elif s[i+1] == ')':
                    i += 2
                else:
                    missing += 1
                    i += 1
                
                if balance < 0:
                    missing += 1
                    balance = 0
        
        return missing + 2 * balance
        