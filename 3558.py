class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        mod = 1000000007
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, prev):
            d = 0
            for c in graph[node]:
                if c != prev:
                    d = max(d, dfs(c, node) + 1)
            return d

        return pow(2, dfs(1, 0) - 1, mod)
