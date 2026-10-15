class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = set()
        queue = [["1"] * n, ["0"] + ["1"] * (n-1), ["1"] * (n-1) + ["0"]]
        if n > 2:
            queue.append(["0"] + ["1"] * (n-2) + ["0"])

        while queue:
            curr = queue[0]
            queue = queue[1:]
            result.add("".join(curr))

            for i in range(1, len(curr)-1):
                if curr[i-1] == "1" and curr[i+1] == "1":
                    cp = curr[:]
                    cp[i] = "0"
                    if "".join(cp) not in result:
                        queue.insert(0,cp)
                

        return result

