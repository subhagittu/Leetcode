class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        n = len(matrix[0])
        height = [0]*n
        ans = 0

        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in range(n+1):
                cur = height[i] if i < n else 0
                while stack and height[stack[-1]] > cur:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    ans = max(ans, h*w)
                stack.append(i)
        return ans
        
