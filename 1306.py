class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = set()
        q = deque([start])

        while q:
            i = q.popleft()

            if i < 0 or i >= n or i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)
            q.append(i + arr[i])
            q.append(i - arr[i])

        return False
    def canReachDFS(self, arr, start):
        n = len(arr)
        visited = set()

        def dfs(i):
            if i < 0 or i >= n or i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)

