class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        min_diff = float('inf')
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_diff:
                min_diff = arr[i] - arr[i-1]
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                ans.append([arr[i-1], arr[i]])
        
        return ans