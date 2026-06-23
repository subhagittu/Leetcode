class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int-
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r-l+1
        dp = [1]*m
        for i in range(0,n-1):
            dp.reverse()
            s = 0
            for j in range(0,m):
                dp[j], s = s, (s+dp[j])%MOD

        return (sum(dp)*2)%MOD
