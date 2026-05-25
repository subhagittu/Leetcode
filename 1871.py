class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            # add new index entering window
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            # remove old index leaving window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            dp[i] = (reachable > 0 and s[i] == '0')

        return dp[n - 1]
        
