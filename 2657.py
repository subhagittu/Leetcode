class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = [0] * n
        seen = [0] * (n + 1)
        
        for i in range(n):
            seen[0] += seen[A[i]]
            seen[A[i]] = 1
            
            seen[0] += seen[B[i]]
            seen[B[i]] = 1
            
            res[i] = seen[0]
            
        return res
