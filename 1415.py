class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []

        def dfs(path):
            if len(path) == n:
                res.append(path)
                return

            for char in "abc":
                if path == "" or path[-1] != char:
                    dfs(path+char)
            
        dfs("")

        if k > len(res):
            return ""

        return res[k-1]
