class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()

        for s in strs:
            code = tuple(sorted(list(s)))
            if code in anagrams:
                anagrams[code].append(s)
            else:
                anagrams[code] = [s]
        
        return anagrams.values()