import math
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd1 = 1
        sumodd = 0

        for i in range(n):
            sumodd += odd1
            odd1 += 2

        even1 = 2
        sumeven = 0

        for i in range(n):
            sumeven += even1
            even1 += 2
        while sumeven != 0:
            sumodd, sumeven = sumeven, sumodd % sumeven

        return sumodd



        
        