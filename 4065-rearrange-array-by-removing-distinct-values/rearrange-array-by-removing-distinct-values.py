from collections import defaultdict

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        counter = defaultdict(int)
        byReps = defaultdict(list)

        for n in nums:
            counter[n] += 1
            byReps[counter[n]].append(n)
        
        if len(counter.values()) <= 1:
            return nums
        if len(byReps.values()) <= 1:
            return sorted(nums)

        sortedByReps = sorted(byReps.keys())

        for i in range(len(sortedByReps)-1):
            result += sorted(byReps[sortedByReps[i]]) * (sortedByReps[i+1] - sortedByReps[i])
        
        result += sorted(byReps[sortedByReps[-1]]) * (sortedByReps[-1] - sortedByReps[-2])
        return result
