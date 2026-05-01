class Solution(object):
    def sumarr(self,arr):
        sum1 = 0
        for i,ele in enumerate(arr):
            sum1 += ele*i

        return sum1
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        res.append(nums[:])
        k = len(nums)
        i = 0
        while i != len(nums):
            n1 = nums[-1]
            nums.pop(-1)
            nums.insert(0,n1)
            res.append(nums[:])
            i += 1
        
        max1 = float('-inf')

        for arr in res:
            max1 = max(max1,self.sumarr(arr))

        return max1
            

