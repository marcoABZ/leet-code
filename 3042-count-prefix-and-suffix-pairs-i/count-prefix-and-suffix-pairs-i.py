class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False

            i, j, k = 0, len(str2)-1, len(str1)-1
            while i < len(str1):
                if str2[i] != str1[i] or str2[j] != str1[k]:
                    return False
                i += 1
                j -= 1
                k -= 1
            return True
        
        result = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        
        return result