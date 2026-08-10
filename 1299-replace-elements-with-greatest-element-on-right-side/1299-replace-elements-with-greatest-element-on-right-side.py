class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        maxRight = arr[-1]  

        res = []
        res.append(-1)
        for i in range(n - 1, 0, -1):
           
            current = arr[i]
           
            
            
            maxRight = max(maxRight, current)
            res.append(maxRight)
        
        return res[::-1]