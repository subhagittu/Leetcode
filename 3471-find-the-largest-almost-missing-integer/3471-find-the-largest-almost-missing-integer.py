class Solution(object):
    def largestInteger(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = [0] * 51
        for x in A:
            f[x] += 1

        res, n = -1, len(A)
        for i, c in enumerate(A):
            if k == n or (f[c]==1 and (k==1 or not i or i+1==n)):
                res = max(res, c)

        return res