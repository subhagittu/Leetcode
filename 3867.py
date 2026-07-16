#from math import gcd
#1
class Solution(object):
    def gcd(self,a,b):
        while a!= 0:
            b, a = a, b%a
        return b
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixGCD = []

        mx = float('-inf')

        for num in nums:
            mx = max(mx, num)
            prefixGCD.append(self.gcd(mx, num))

        prefixGCD.sort()

        i, j = 0, len(prefixGCD) - 1
        ans = 0

        while i < j:
            ans += self.gcd(prefixGCD[i], prefixGCD[j])
            i += 1
            j -= 1

        return ans
