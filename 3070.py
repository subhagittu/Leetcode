#optimal approach
#O(n^3) complexity
class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                total = 0
                
                # calculate sum from (0,0) to (i,j)
                for r in range(i + 1):
                    for c in range(j + 1):
                        total += grid[r][c]
                
                if total <= k:
                    count += 1
        
        return count
