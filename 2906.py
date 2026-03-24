class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        arr = []
        for i in range(0,rows):
            for j in range(0,cols):
                arr.append(grid[i][j])

        size = len(arr)
        pref = [1]*size
        suff = [1]*size

        for i in range(1,size):
            pref[i] = (pref[i-1]*arr[i-1])%12345

        for i in range(size-2,-1,-1):
            suff[i] = (suff[i+1]*arr[i+1])%12345

        res = [(pref[i]*suff[i])%12345 for i in range(size)]

        ans = [[0]*cols for _ in range(rows)]
        idx = 0
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = res[idx]
                idx += 1

        return ans
