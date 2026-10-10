class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = dict()

        for i, num in enumerate(nums):
            if num in counter:
                counter[num] = (counter[num][0] + 1, counter[num][1] + [i])
            else:
                counter[num] = (1, [i])
        
        return len([v for v in counter.values() if v[0] == 3 and v[1][1] - v[1][0] == v[1][2] - v[1][1]])