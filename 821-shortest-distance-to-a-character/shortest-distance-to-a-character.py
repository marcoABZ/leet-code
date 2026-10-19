class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        st = []
        result = [len(s)] * len(s)

        for i, cc in enumerate(s):
            if cc == c:
                result[i] = 0
                for ss in st:
                    result[ss] = i - ss
                st = []
            else:
                st.append(i)
        st = []

        for i, cc in enumerate(s[::-1]):
            if cc == c:
                for ss in st:
                    result[len(s) - ss - 1] = min(result[len(s) - ss - 1], i-ss)
                st = []
            else:
                st.append(i)

        return result
