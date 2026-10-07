class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c.isdigit() and stack:
                stack = stack[:-1]
                continue
            stack.append(c)
        
        return ''.join(stack)