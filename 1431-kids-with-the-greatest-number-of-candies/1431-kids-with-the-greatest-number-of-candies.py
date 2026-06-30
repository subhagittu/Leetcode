class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l1 = []
        maxnum = max(candies)
        for ele in candies:
            if ele+extraCandies >= maxnum:
                l1.append(True)
            else:
                l1.append(False)
        return l1
        