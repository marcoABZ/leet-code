class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]

        for ast in asteroids[1:]:
            if ast > 0:
                stack.append(ast)
                continue
            
            while True:
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                    break
                elif abs(ast) > abs(stack[-1]):
                    stack = stack[:-1]
                elif abs(ast) == abs(stack[-1]):
                    stack = stack[:-1]
                    break
                else:
                    break
        
        return stack