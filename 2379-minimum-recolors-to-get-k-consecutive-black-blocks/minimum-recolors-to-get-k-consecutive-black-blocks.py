class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        whites = 0
        result = 0

        for i, b in enumerate(blocks):
            if i < k:
                if b == 'W':
                    whites += 1
                    result += 1
                continue
            
            if b == 'W':
                whites += 1
            if blocks[i-k] == 'W':
                whites -= 1

            result = min(result, whites)
        
        return result
                