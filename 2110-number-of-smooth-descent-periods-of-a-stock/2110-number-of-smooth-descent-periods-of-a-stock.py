class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        size = len(prices)
        i = 0
        j = i + 1
        for j in range(1,size):
            
            if prices[j] == prices[j-1]-1:
                ans += (j-i)
                j += 1
            else:
                i = j
                j = i+1
        return ans + size