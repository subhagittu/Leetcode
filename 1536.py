class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        zeroCount = OrderedDict()

        for row in range(n):
            count = 0
            for col in range(n-1,-1,-1):
                if grid[row][col] == 1:
                    break
                count+=1

            zeroCount[row] = count
        
        swap = 0

        for row in range(n):
            for i ,(col,count) in enumerate(zeroCount.items()):
                if count>=n-row-1:
                    swap+=i
                    zeroCount.pop(col)
                    break
                if i == len(zeroCount)-1:
                    return -1
        return swap





        
