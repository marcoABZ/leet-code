class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a, b = [], []

        for i, n in enumerate(nums):
            if i == 0:
                a.append(n)
            elif i == 1:
                b.append(n)
            else:
                if a[-1] > b[-1]:
                    a.append(n)
                else:
                    b.append(n)
            
        return a + b