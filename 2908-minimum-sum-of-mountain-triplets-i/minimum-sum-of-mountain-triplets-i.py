class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_min, r_min = [], []
        i, j = 0, len(nums) - 1
        while i < len(nums):
            if not l_min:
                l_min.append(nums[i])
                r_min.append(nums[j])
            else:
                l_min.append(min(nums[i], l_min[-1]))
                r_min.insert(0, min(r_min[0], nums[j]))
            i += 1
            j -= 1
        
        print(l_min, r_min)
        top = -1
        for i in range(1,len(nums)-1):
            print(i, nums[i], l_min[i], r_min[i])
            if l_min[i] < nums[i] and r_min[i] < nums[i]:
                if top == -1:
                    top = nums[i] + l_min[i] + r_min[i]
                else:
                    top = min(top, nums[i] + l_min[i] + r_min[i])

        return top