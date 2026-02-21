class Solution(object):
    def isprime(self,num):
        if num < 2:
            return False
        for i in range(2,num//2 +1):
            if num%i == 0:
                return False
        return True


        
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        cnt = 0
        
        for n in range(left,right+1):
            binary = ""
            n1 = n
            if n1 == 0:
                binary = '0'
            else:
                while n > 0:
                    binary = str(n%2)+binary
                    n = n//2
            if self.isprime(binary.count('1')):
                cnt += 1

        return cnt

            
