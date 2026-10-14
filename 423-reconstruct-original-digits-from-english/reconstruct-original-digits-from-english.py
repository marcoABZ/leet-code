from collections import defaultdict

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = defaultdict(int)
        res = [0] * 10

        for c in s:
            if c == 'z':
                res[0] += 1
                counter['e'] -= 1
                counter['r'] -= 1
                counter['o'] -= 1
            elif c == 'w':
                res[2] += 1
                counter['t'] -= 1
                counter['o'] -= 1
            elif c == 'u':
                res[4] += 1
                counter['f'] -= 1
                counter['o'] -= 1
                counter['r'] -= 1
            elif c == 'x':
                res[6] += 1
                counter['s'] -= 1
                counter['i'] -= 1
            elif c == 'g':
                res[8] += 1
                counter['e'] -= 1
                counter['i'] -= 1
                counter['h'] -= 1
                counter['t'] -= 1
            else:
                counter[c] += 1
        
        if counter['o']:
            res[1] = counter['o']
            counter['n'] -= counter['o']
            counter['e'] -= counter['o']
            counter['o'] -= counter['o']

        if counter['h']:
            res[3] = counter['h']
            counter['t'] -= counter['h']
            counter['r'] -= counter['h']
            counter['e'] -= 2 * counter['h']
            counter['h'] -= counter['h']
        
        if counter['f']:
            res[5] = counter['f']
            counter['i'] -= counter['f']
            counter['v'] -= counter['f']
            counter['e'] -= counter['f']
            counter['f'] -= counter['f']

        if counter['s']:
            res[7] = counter['s']
            counter['e'] -= 2 * counter['s']
            counter['v'] -= counter['s']
            counter['n'] -= counter['s']

        res[9] = counter['i']
        result = ""
        for i, v in enumerate(res):
            result += str(i) * res[i]
        
        return result