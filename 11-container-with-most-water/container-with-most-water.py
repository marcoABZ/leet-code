class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        top = 0

        while i < j:
            curr = min(height[i], height[j]) * (j - i)
            top = max(top, curr)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return top