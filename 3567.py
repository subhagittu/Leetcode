class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        
        ans = []
        
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                
                # Step 1: collect elements in k x k submatrix
                vals = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                # Step 2: take distinct values
                vals = list(set(vals))
                
                # Step 3: if only one element → answer is 0
                if len(vals) <= 1:
                    row.append(0)
                    continue
                
                # Step 4: sort values
                vals.sort()
                
                # Step 5: find minimum absolute difference
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t - 1])
                
                row.append(min_diff)
            
            ans.append(row)
        
        return ans
        
