class Solution:
    def maxProduct(self, s: str) -> int:
        def isPalindromic(s):
            i, j = 0, len(s)-1

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        subseqs = []

        for i, c in enumerate(s):
            adds = [(c, set([i]))]
            for sub, idx in subseqs:
                idx = idx.copy()
                idx.add(i)
                adds.append((sub + c, idx))
            subseqs += adds
        

        subseqs = [s for s in subseqs if isPalindromic(s[0])]
        result = 0
        for i in range(len(subseqs)):
            for j in range(1, len(subseqs)):
                a, idxA = subseqs[i]
                b, idxB = subseqs[j]

                if not (idxA & idxB):
                    result = max(len(a) * len(b), result)

        return result