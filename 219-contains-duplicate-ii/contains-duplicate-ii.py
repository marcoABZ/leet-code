class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = dict()

        for i, n in enumerate(nums):
            if i <= k:
                if n in counter:
                    if counter[n]:
                        return True
                    counter[n] += 1
                else:
                    counter[n] = 1
                continue
            
            counter[nums[i-k-1]] -= 1
            if n in counter:
                if counter[n]:
                    return True
                counter[n] += 1
            else:
                counter[n] = 1
        
        return False