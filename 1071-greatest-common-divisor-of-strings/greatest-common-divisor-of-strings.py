class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        prefix_size = 1
        result = ""

        while prefix_size <= len(str1)and prefix_size <= len(str2):
            if len(str1) % prefix_size != 0 or len(str2) % prefix_size != 0:
                prefix_size += 1
                continue

            prefix = str1[:prefix_size]
            valid = True

            i, j = 0, prefix_size
            while j <= len(str1):
                if str1[i:j] != prefix:
                    valid = False
                    break
                i, j = j, j + prefix_size
            if i != len(str1):
                valid = False
            
            
            i, j = 0, prefix_size
            while valid and j <= len(str2):
                if str2[i:j] != prefix:
                    valid = False
                    break
                i, j = j, j + prefix_size
            if i != len(str2):
                valid = False

            if valid:
                result = prefix
            
            prefix_size += 1
        
        return result
        