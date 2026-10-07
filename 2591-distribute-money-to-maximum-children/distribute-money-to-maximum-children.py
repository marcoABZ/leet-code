class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        best = children

        while best >= 0:
            # Not enough money
            if money - (best * 8) < (children - best):
                best -= 1
            # Enough money, but not evenly split in 8s
            elif (children - best) == 0 and (money - (best * 8)) > 0:
                best -= 1
            # Enough money, but last child would receive 4
            elif (children - best) == 1 and (money - (best * 8)) == 4:
                best -= 1
            else:
                return best
    
        return best
        