class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            k = 1
            while k <= len(stack) and temp > stack[-k][0]:
                _, id = stack[-k]
                result[id] = i - id 
                k += 1
            
            if k > 1:
                stack = stack[:-k+1]
            stack.append((temp, i))
        
        return result
