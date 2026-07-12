class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d1 = {}
        ranks = 1
        arr1 = []
        arr1 = set(arr)
        arr1 = list(arr1)
        arr1.sort()
        for ele in arr1:
            d1[ele] = ranks
            ranks += 1
        res = []
        
        for ele in arr:
            res.append(d1[ele])

        return res