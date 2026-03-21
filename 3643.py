class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(k // 2):
            row1 = grid[x + i]
            row2 = grid[x + k - 1 - i]
            for j in range(k):
                row1[y + j], row2[y + j] = row2[y + j], row1[y + j]
        
        return grid
        
