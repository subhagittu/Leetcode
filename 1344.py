class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        x = hour + minutes / 60.0
        diff = (11 * x) % 12
        return min(diff, 12 - diff) * 30
