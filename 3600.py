class Solution(object):
    def maxStability(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        def append_edge(u, v):
            if used[u] == used[v] == -1:
                    used[u] = used[v] = len(components)
                    components[len(components)] = [u, v]
            elif used[u] == -1:
                used[u] = used[v]
                components[used[v]].append(u)
            elif used[v] == -1:
                used[v] = used[u]
                components[used[u]].append(v)
            else:
                _from = components[used[v]]
                _to = components[used[u]]
                while _from:
                    t = _from.pop()
                    _to.append(t)
                    used[t] = used[u]
        used = [-1] * n
        stability = 999999999
        optional = []
        components = {}
        for u, v, s, must in edges: 
            if must:
                if used[u] >= 0 and used[v] >= 0 and used[u] == used[v]:  # cicle
                    return -1
                append_edge(u, v)
                if s < stability:
                    stability = s
            else:
                optional.append([s, u, v]) 
        optional.sort(reverse=True)
        otional_added = []
        for s, u, v in optional:
            if used[u] != used[v] or used[u] == used[v] == -1:
                append_edge(u, v)
                otional_added.append(s)
        if any(used[0] != u for u in used):
            return -1
        for s in otional_added[::-1]:
            if k:
                k -= 1
                s += s
            if s < stability:
                stability = s
        return stability
        
