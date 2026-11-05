class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        def far(a):  # no b in [a - d, a + d]
            return all(abs(a - b) > d for b in arr2)

        return sum(map(far, arr1))
        