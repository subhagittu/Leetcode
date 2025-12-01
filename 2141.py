class Solution(object):
    def maxRunTime(self, n, batteries):
        totalEnergy = sum(batteries)
        batteries.sort()

        i = len(batteries) - 1
        while i >= 0:
            if batteries[i] > totalEnergy // n:
                totalEnergy -= batteries[i]
                n -= 1
            else:
                break
            i -= 1

        return totalEnergy // n
