class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_a, stack_b = [], []

        for c in s:
            if c == "#":
                if stack_a:
                    stack_a = stack_a[:-1]
                continue
            stack_a.append(c)
        
        for c in t:
            if c == "#":
                if stack_b:
                    stack_b = stack_b[:-1]
                continue
            stack_b.append(c)
        
        return "".join(stack_a) == "".join(stack_b)