class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ops = 0
        score = None

        for i in range(0, len(nums)-1, 2):
            sc = nums[i] + nums[i+1]

            if score is None:
                score = sc
            elif sc != score:
                return ops

            ops +=1
        
        return ops