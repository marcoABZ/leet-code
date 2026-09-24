class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)

        curr = chars[0]
        repeat = 1
        result = 0
        i = 0

        for c in chars[1:]:
            if c == curr:
                repeat += 1
                continue
            
            chars[i] = curr
            i += 1
            result += 1

            if repeat > 1:
                j = 0
                while repeat > 0:
                    chars.insert(i, str(repeat % 10))
                    repeat /= 10
                    j += 1
                i += j
                result += j
            
            repeat = 1
            curr = c

        chars[i] = curr
        i += 1
        result += 1

        if repeat > 1:
            j = 0
            while repeat > 0:
                chars.insert(i, str(repeat % 10))
                repeat /= 10
                j += 1
            i += j
            result += j

        return result
        