class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = n + 1

        dp = [INF] * n

        left = 0
        total = 0
        ans = INF

        for right in range(n):

            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:

                length = right - left + 1

                if left > 0 and dp[left - 1] != INF:
                    ans = min(
                        ans,
                        length + dp[left - 1]
                    )

                dp[right] = length

            if right > 0:
                dp[right] = min(
                    dp[right],
                    dp[right - 1]
                )

        return -1 if ans == INF else ans