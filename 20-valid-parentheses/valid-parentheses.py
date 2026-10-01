class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            if not stack:
                return False
            if (c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{'):
                stack = stack[:-1]
                continue
            return False
        
        return not stack