class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minum = prices[0]
        for ele in prices:
            if ele < minum:
                minum = ele
            else:
                if ele - minum > profit:
                    profit = ele - minum

        return profit