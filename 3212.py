class Solution(object):
    def numberOfSubmatrices(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(0,rows):
            for j in range(0,cols):
                countx = 0
                county = 0

                for r in range(i+1):
                    for c in range(j+1):
                        if grid[r][c] == 'X':
                            countx += 1

                        elif grid[r][c] == 'Y':
                            county += 1

                if countx == county and countx > 0 :
                    count += 1

        return count
