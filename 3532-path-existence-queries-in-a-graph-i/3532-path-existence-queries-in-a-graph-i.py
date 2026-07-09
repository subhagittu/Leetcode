class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        comp = [0]*n
        res = []
        for i in range(1,n):
            if nums[i]-nums[i-1] <= maxDiff:
                comp[i] = comp[i-1]
            else:
                comp[i] = comp[i-1] + 1

        for u,v in queries:
            if comp[u] == comp[v]:
                res.append(True)
            else:
                res.append(False)

        return res
