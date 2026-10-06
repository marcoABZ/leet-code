class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = set()
        curr_num = None

        if word[0].isdigit():
            curr_num = int(word[0])

        for i, c in enumerate(word[1:]):
            if c.isalpha():
                if not curr_num is None:
                    result.add(curr_num)
                curr_num = None
            else:
                if curr_num is None:
                    curr_num = int(c)
                else:
                    curr_num *= 10
                    curr_num += int(c)
        
        if not curr_num is None:
            result.add(curr_num)
        return len(result)
