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



#-------------------------------------------------------------------------------------------------------------------------------------------------

#Optimized one - 


class Solution:
    def sumFourDivisors(self, nums):
        total = 0
        for n in nums:
            root1 = int(n**0.5)
            sum1 = 0
            cnt = 0
            for i in range(1,root1+1):
                if n%i==0:
                    j = n//i
                
                    if i == j:
                        sum1 += i
                        cnt += 1
                    else:
                        cnt += 2
                        sum1 += i + j

                if cnt > 4:
                    break
            if cnt == 4:
                total += sum1
        return total



        
        
            

        return sum1


        
