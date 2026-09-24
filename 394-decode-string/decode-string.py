class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        multipliers = []
        sequences = []

        i = 0
        result = ""
        
        while i < len(s):
            if s[i].isdigit():
                mult = 0
                while s[i].isdigit():
                    mult *= 10
                    mult += int(s[i])
                    i += 1
                multipliers.append(mult)
                mult = 0
                continue
            
            if s[i] == "[":
                i += 1
                seq = ""
                while s[i].isalpha():
                    seq += s[i]
                    i += 1
                sequences.append(seq)
                seq = ""
                continue
            
            if s[i] == "]":
                curr = sequences[-1] * multipliers[-1]
                sequences = sequences[:-1]
                multipliers = multipliers[:-1]
                if sequences:
                    sequences[-1] += curr
                else:
                    result += curr
                i += 1
                continue

            if sequences:
                sequences[-1] += s[i]
            else:
                result += s[i]
            i += 1
        
        return result
        