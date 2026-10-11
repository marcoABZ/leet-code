class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        toggle = { i: False for i in range(1,101) }

        for bulb in bulbs:
            toggle[bulb] = not toggle[bulb]
        
        return sorted([k for k, v in toggle.items() if v])