class Solution(object):
    def divisors1(self,num):
        l1 = []
        for i in range(1,num+1):
            if num%i==0:
                l1.append(i)
        return l1





    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1 = []
        sum1 = 0
        for eles in nums:
            l2 = []
            l2 = self.divisors1(eles)
            if len(l2) == 4:
                sum1 += sum(l2)

        
            

        return sum1


        
