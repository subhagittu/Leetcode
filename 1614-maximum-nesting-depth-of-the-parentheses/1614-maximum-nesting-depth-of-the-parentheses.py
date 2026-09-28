class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        r = 0
        for c in s:
            if c == ')':
                depth -= 1
                continue
            
            if c != '(':
                continue
            depth += 1
            
            if depth > r:
                r = depth
        return r