class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j = len(digits) - 1

        while j >= 0:
            if digits[j] == 9:
                digits[j] = 0
                j -= 1
                continue

            digits[j] += 1
            break
        
        if j < 0:
            digits.insert(0, 1)
        
        return digits


