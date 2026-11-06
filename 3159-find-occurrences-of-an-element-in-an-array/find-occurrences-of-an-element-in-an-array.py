class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ocs = dict()
        i = 1

        for j, n in enumerate(nums):
            if n == x:
                ocs[i] = j
                i += 1
        
        result = []
        for q in queries:
            if q >= i:
                result.append(-1)
            else:
                result.append(ocs[q])
        
        return result