class Solution(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        vals = [(grid[i][j],i,j) for i in range(m) for j in range(n)]
        vals.sort(reverse = True)
        def forward(dp):
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        dp[i][j] = min(dp[i][j],dp[i-1][j] + grid[i][j])
                    
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        
        dp = [[float('inf')]*n for _ in range(m)]
        dp[0][0] = 0
        forward(dp)
   
        for _ in range(k):
            dp2 = [rows[:] for rows in dp]
            vals = []
            for i in range(m):
                for j in range(n):
                    vals.append((grid[i][j], dp2[i][j], i, j))
            vals.sort(key= lambda x:(-x[0],x[1]))
            min_val = 10**8
            for val, _, i, j in vals:
                if dp[i][j] < min_val:
                    min_val = dp[i][j]
                
                if dp2[i][j] > min_val:
                    dp2[i][j] = min_val
            forward(dp2)
            dp = dp2
            
        return dp[-1][-1]
            
