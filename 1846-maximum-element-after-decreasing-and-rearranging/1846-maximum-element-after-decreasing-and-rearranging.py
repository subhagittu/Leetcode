class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        freq = [0] * (n + 1)

        for x in arr:
            freq[min(x, n)] += 1

        res = 1
        for i in range(2, n + 1):
            res = min(res + freq[i], i)

        return res