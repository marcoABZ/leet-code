class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        counter_a = {}
        counter_b = {}

        for c in word1:
            if c in counter_a:
                counter_a[c] += 1
            else:
                counter_a[c] = 1
        
        for c in word2:
            if c in counter_b:
                counter_b[c] += 1
            else:
                counter_b[c] = 1
        
        values_a = sorted(counter_a.values())
        values_b = sorted(counter_b.values())

        if len(values_a) != len(values_b):
            return False

        for k in counter_a.keys():
            if k not in counter_b:
                return False

        for i in range(len(values_a)):
            if values_a[i] != values_b[i]:
                return False
        
        return True