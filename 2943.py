class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def longest_consecutive(arr):
            arr.sort()
            maxlength = curr = 1
            for i in range(1,len(arr)):
                if arr[i] == arr[i-1]+1:
                    curr += 1
                    maxlength = max(maxlength,curr)
                else:
                    curr = 1

            return maxlength
        side = min(longest_consecutive(hBars),longest_consecutive(vBars))+1
        return side*side
