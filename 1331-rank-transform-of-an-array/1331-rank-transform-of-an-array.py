class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {}
        rank = 1
        arr1 = []
        arr1[:] = set(arr)
        arr1[:] = list(arr1)
        arr1.sort()
        for x in arr1:
            ranks[x] = rank
            rank += 1
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr