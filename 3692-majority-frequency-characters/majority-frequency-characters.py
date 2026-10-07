class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = dict()

        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        groups = dict()
        for k, v in counter.items():
            if v in groups:
                groups[v].append(k)
            else:
                groups[v] = [k]
        
        top_freq = 0
        top_size = 0
        result = None

        for k, v in groups.items():
            if len(v) > top_size:
                top_freq = k
                top_size = len(v)
                result = v
            elif len(v) == top_size:
                if k > top_freq:
                    top_freq = k
                    result = v
        
        return "".join(result)