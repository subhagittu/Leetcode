class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        A = colors
        n = len(A)
        left, right = 0, n - 1

        for i in range(n):
            if A[i] ^ A[-1]:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if A[i] ^ A[0]:
                right = i
                break

        return max(n - 1 - left, right)
            
