class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ["0", "1"]
        
        while True:
            if len(result[0]) == n:
                break

            curr = result.pop(0)
            if curr[-1] == "0":
                result.append(curr + "1")
            else:
                result.append(curr + "0")
                result.append(curr + "1")     

        return result

