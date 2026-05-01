class Solution(object):
    # def sumarr(self,arr):
    #     sum1 = 0
    #     for i,ele in enumerate(arr):
    #         sum1 += ele*i

    #     return sum1
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a_sum = 0
        A = nums[:]
        F = 0
        n = len(A)

        for i in range(n):
            a_sum += A[i]
            F += i * A[i]

        res = F

        for i in range(1, n):
            F += a_sum - n * A[-i]
            res = max(res, F)

        return res
