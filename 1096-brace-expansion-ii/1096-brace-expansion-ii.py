class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        ans = set()

        def dfs(s):
            r = s.find('}')

            # No braces left
            if r == -1:
                ans.add(s)
                return

            # Find matching '{'
            l = s.rfind('{', 0, r)

            left = s[:l]
            right = s[r + 1:]

            # Content inside { }
            inside = s[l + 1:r]

            for part in inside.split(','):
                dfs(left + part + right)

        dfs(expression)
        return sorted(ans)