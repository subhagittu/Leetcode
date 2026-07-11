class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n

        def dfs(u, comp):
            vis[u] = True
            comp.append(u)
            for v in adj[u]:
                if not vis[v]:
                    dfs(v, comp)

        ans = 0
        for i in range(n):
            if not vis[i]:
                comp = []
                dfs(i, comp)
                if all(len(adj[u]) == len(comp) - 1 for u in comp):
                    ans += 1

        return ans