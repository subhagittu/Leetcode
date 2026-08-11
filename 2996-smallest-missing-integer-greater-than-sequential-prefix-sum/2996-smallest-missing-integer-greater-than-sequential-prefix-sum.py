class Solution(object):
    def missingInteger(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(A)
        seen = set(A)
        sum = A[0]

        for i in range(1, n):
            if A[i] == A[i - 1] + 1:
                sum += A[i]
            else:
                break

        while sum in seen:
            sum += 1

        return sum