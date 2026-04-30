class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):

                    if dp[i][j][c] == -1:
                        continue

                    # move down
                    if i + 1 < m:
                        val = grid[i+1][j]
                        cost = 0 if val == 0 else 1

                        nc = c + cost
                        if nc <= k:
                            dp[i+1][j][nc] = max(
                                dp[i+1][j][nc],
                                dp[i][j][c] + val
                            )

                    # move right
                    if j + 1 < n:
                        val = grid[i][j+1]
                        cost = 0 if val == 0 else 1

                        nc = c + cost
                        if nc <= k:
                            dp[i][j+1][nc] = max(
                                dp[i][j+1][nc],
                                dp[i][j][c] + val
                            )

        ans = -1
        for c in range(k+1):
            ans = max(ans, dp[m-1][n-1][c])

        return ans
