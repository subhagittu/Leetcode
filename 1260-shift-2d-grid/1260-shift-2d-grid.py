class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                
                oldIndex = i * n + j

                
                newIndex = (oldIndex + k) % total

                
                newRow = newIndex // n
                newCol = newIndex % n

                ans[newRow][newCol] = grid[i][j]

        return ans