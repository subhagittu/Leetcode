class Solution(object):
    def hasValidPath(self, A):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(A), len(A[0])

        if ~(m + n) & 1 or A[0][0] == ")" or A[-1][-1] == "(":
            return False

        dp = defaultdict(set)
        dp[0, 0] = {0}

        for i in range(m):
            for j in range(n):
                v = 1 - ((ord(A[i][j]) & 1) << 1)

                for d in dp[i, j]:
                    nk = d + v

                    if nk > -1:
                        dp[i + 1, j].add(nk)
                        dp[i, j + 1].add(nk)

        return 0 in dp[m, n - 1]