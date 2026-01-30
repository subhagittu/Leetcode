from typing import List
import math

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        n = len(source)
        strings = set(original) | set(changed)
        idx = {s: i for i, s in enumerate(strings)}
        m = len(strings)
        dist = [[math.inf] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        length_map = {}
        for o, c in zip(original, changed):
            length_map.setdefault(len(o), []).append((o, c))
        dp = [math.inf] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            else:
                if source[i] in idx and target[i] in idx:
                    dp[i] = dp[i + 1] + dist[idx[source[i]]][idx[target[i]]]
            for L, pairs in length_map.items():
                if i + L > n:
                    continue

                s = source[i:i + L]
                t = target[i:i + L]

                if s in idx and t in idx:
                    dp[i] = min(dp[i], dp[i + L] + dist[idx[s]][idx[t]])

        return -1 if dp[0] == math.inf else dp[0]
