class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        
        arr = [num for row in grid for num in row]
        
        # Step 1: check if possible
        for num in arr:
            if (num - arr[0]) % x != 0:
                return -1
        
        # Step 2: normalize
        arr = [num // x for num in arr]
        
        # Step 3: find median
        arr.sort()
        median = arr[len(arr)//2]
        
        # Step 4: count operations
        return sum(abs(num - median) for num in arr)
