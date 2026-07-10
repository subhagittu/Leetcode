class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        total = high - low + 1
        if low % 2 != 0 and high % 2 != 0:
            return total // 2 + 1
        return total // 2