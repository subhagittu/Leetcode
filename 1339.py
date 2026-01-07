class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.best = 0

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.best = max(self.best, s * (total - s))
            return s

        dfs(root)
        return self.best % MOD
