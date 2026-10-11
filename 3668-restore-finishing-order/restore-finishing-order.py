class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        positions = {
            n: i for i, n in enumerate(order)
        }

        finishes = sorted([(positions[n], n) for n in friends])

        return [n[1] for n in finishes]
